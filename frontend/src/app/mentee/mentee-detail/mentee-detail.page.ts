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
  selector: 'app-mentee-detail',
  templateUrl: './mentee-detail.page.html',
  styleUrls:  ['./mentee-detail.page.scss']
})
export class MenteeDetailPage {
  private todo : FormGroup;
  private readonly API_URL = 'http://brasa-pre.herokuapp.com/api';
  public satArray:any=[];
  public scoresArray:any=[];
  public satSubjectsArray:any=[];
 AddSAT(){
   this.satArray.push({'value':''});
 };
 AddScore(){
   this.scoresArray.push({'name':'','value':''});
 };
 AddSubjects(){
   this.satSubjectsArray.push({'subject':'','value':'','date':''});
 }
 private headers: HttpHeaders;
  constructor( private formBuilder: FormBuilder, private http: HttpClient  ) {
    this.headers = new HttpHeaders({'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT',
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
    });
    this.todo = this.formBuilder.group({
      //title: ['', Validators.required],
      "username": '',
      //mentor: '',
      //city: '',
      //state: '',
      //financial_aid: ''
      //description: [''],
    });
  }
  public logForm(){
    console.log(this.todo.value)
    console.log(this.http.post(`${this.API_URL}/pre_users`, this.todo.value, {headers: this.headers}))
    this.http.post(`${this.API_URL}/pre_users`, this.todo.value, {headers: this.headers}).subscribe(data => {
        console.log(data['_body']);
       }, error => {
        console.log(error);
      });
  }

  //mentee: Mentee;

  /*constructor(private route: ActivatedRoute,
              private menteeService: MenteeService,
              private loaderService: LoaderService,
              private alertSerice: AlertService) { }*/

    /*ionViewWillEnter() {
    const menteeId = this.route.snapshot.paramMap.get('menteeId');

    this.loaderService.presentLoading();
    this.menteeService.getMenteeById(menteeId).subscribe(
      (mentee: Mentee[]) => {

        this.mentee = mentee.map((mentee: Mentee) => {
          mentee.text = this.menteeService.replaceMenteeTextLine(mentee.text);

          return mentee;
        })[0];


        this.loaderService.dismissLoading();
    });
  }
  */
  /*
  updateImage() {
    this.mentee.img = 'assets/image/DefaultMentee.png'

  }
  */

}
