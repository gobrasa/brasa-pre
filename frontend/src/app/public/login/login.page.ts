import { AuthenticationService } from './../../services/authentication.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  constructor(private authService: AuthenticationService) { }

  ngOnInit() {
  }

  login() {
	var email = (<HTMLInputElement>document.getElementById("Email")).value;
	var password = (<HTMLInputElement>document.getElementById("Password")).value;
    this.authService.login(email, password);
  }

}
