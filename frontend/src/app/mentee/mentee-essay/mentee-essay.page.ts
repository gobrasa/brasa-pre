import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Http, Headers } from '@angular/http'
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router'
import { MenteeService } from '../shared/mentee.service';
import { Mentee } from '../shared/mentee.model'
import { LoaderService } from '../../shared/service/loader.service'
import { AlertService } from '../../shared/service/alert.service'
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import {Validators, FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-mentee-essay',
  templateUrl: './mentee-essay.page.html',
  styleUrls:  ['./mentee-essay.page.scss']
})
export class MenteeEssayPage {
  private todo : FormGroup;
  private readonly API_URL = 'http://brasa-pre.herokuapp.com/api';
  public essayArray:any=[];
  private headers: HttpHeaders;

 AddEssay(){
   this.essayArray.push({'link':''});
 };
 RemoveEssay(){
   this.essayArray.pop();
 };


  constructor( private formBuilder: FormBuilder, private http: HttpClient, private getMentee: HttpClient  ) {
    this.headers = new HttpHeaders({'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT',
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
    });
    this.essayArray.push({'link':''});
    this.todo = this.formBuilder.group({});




  }
  public logForm(){
    for (let i =0; i< this.essayArray.length; i++){
      this.http.post(`${this.API_URL}/exams`, this.essayArray[i], {headers: this.headers}).subscribe(data => {
          console.log(data['_body']);
         }, error => {
          console.log(error);
        });
    };
  };
}
