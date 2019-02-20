import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Http, Headers } from '@angular/http';
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { MentorService } from '../shared/mentor.service';
import { Mentor } from '../shared/mentor.model';
import { LoaderService } from '../../shared/service/loader.service';
import { AlertService } from '../../shared/service/alert.service';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import {Validators, FormBuilder, FormGroup } from '@angular/forms';


@Component({
  selector: 'app-mentor-detail',
  templateUrl: './mentor-detail.page.html',
  styleUrls:  ['./mentor-detail.page.scss']
})
export class MentorDetailPage {
  private todo : FormGroup;
  private readonly API_URL = 'http://brasa-pre.herokuapp.com/api';
  private headers: HttpHeaders;
  //mentor: Mentor;


  constructor(private formBuilder: FormBuilder,
              //private route: ActivatedRoute,
              //private mentorService: MentorService,
              //private loaderService: LoaderService,
              //private alertSerice: AlertService
              private http: HttpClient) {
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
  ionViewWillEnter() {
    //const mentorId = this.route.snapshot.paramMap.get('mentorId');

    //this.loaderService.presentLoading();
    /*
    this.mentorService.getMentorById(mentorId).subscribe(
      (mentor: Mentor[]) => {
        /*
        this.mentor = mentor.map((mentor: Mentor) => {
          mentor.text = this.mentorService.replaceMentorTextLine(mentor.text);

          return mentor;
        })[0];


        this.loaderService.dismissLoading();
    });
    */
  }

  updateImage() {
    /*
    this.mentor.img = 'assets/image/DefaultMentor.png'
    */
  }

}
