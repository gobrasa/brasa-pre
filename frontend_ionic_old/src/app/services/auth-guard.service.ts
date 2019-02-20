import { Injectable } from '@angular/core';
import { CanActivate, Router, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { AuthenticationService } from './authentication.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuardService implements CanActivate {

  constructor(private router: Router, 
              public auth: AuthenticationService) {}
 
  canActivate(): boolean {
    console.log('entered can activate from auth guard service');
    return this.auth.isAuthenticated();
  }
  
  canActivate2(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot
  ): boolean {

    const loggedIn = false; // replace with actual user auth checking logic

    if (!loggedIn) {
      console.log('redirecting to /login');
      this.router.navigate(['/login']);
    }

    return loggedIn;
  }
  
}
