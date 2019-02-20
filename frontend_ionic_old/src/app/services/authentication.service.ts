import { Platform } from '@ionic/angular';
import { Injectable } from '@angular/core';
import { Storage } from '@ionic/storage';
import { BehaviorSubject, Observable } from 'rxjs';

const TOKEN_KEY = 'auth-token';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {

  authenticationState = new BehaviorSubject(false);
  private isLoggedIn = false;

  constructor(private storage: Storage, private plt: Platform) { 
    // ToDo - Add check for expiration - if logged in for more than 2h, log out first
    this.plt.ready().then(() => {
      this.checkToken();
    });
  }

  checkToken() {
    this.storage.get(TOKEN_KEY).then(res => {
      if (res) {
        this.authenticationState.next(true);
      }
    })
  }

  login() {
    return this.storage.set(TOKEN_KEY, 'Bearer 1234567').then(() => {
      console.log(TOKEN_KEY);
      this.authenticationState.next(true);
      this.isLoggedIn = true;
    });
    
  }

  logout() {
      return this.storage.remove(TOKEN_KEY).then(() => {
      this.authenticationState.next(false);
      this.isLoggedIn=false;
     });
    
  }

   isAuthenticated() {
     console.log('checked if it is authenticated');
     console.log('auth: ',this.authenticationState.value);
     //return this.authenticationState.value;
     return this.isLoggedIn;
   }
  
   public getAuthStateObserver(): Observable<boolean> {
    return this.authenticationState.asObservable();
  }

}
