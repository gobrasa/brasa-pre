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
import {Validators, FormBuilder, FormGroup, FormControl } from '@angular/forms';
import { NavController } from '@ionic/angular';

@Component({
  selector: 'app-mentee-detail',
  templateUrl: './mentee-detail.page.html',
  styleUrls:  ['./mentee-detail.page.scss']
})
export class MenteeDetailPage {
  public todo : FormGroup;
  private readonly API_URL = 'http://brasa-pre.herokuapp.com';
  //private readonly API_URL = 'http://bce8300d.ngrok.io';
  public satArray:any=[];
  public scoresArray:any=[];
  public satSubjectsArray:any=[];
  private headers: HttpHeaders;
  public menteeProfile:any=[];
  public menteeId:any;
  public menteeDados:any=[];
  /*
 AddSAT(){
   this.satArray.push({'value':''});
 };
 AddScore(){
   this.scoresArray.push({'category':'','subcategory':'', 'score': ''});
 };
 RemoveScore(){
   this.scoresArray.pop();
 };
 AddSubjects(){
   this.satSubjectsArray.push({'subject':'','value':'','date':''});
 }*/

  constructor( private formBuilder: FormBuilder,
    private http: HttpClient,
    private getMentee: HttpClient,
    private menteeService: MenteeService,
    private route: ActivatedRoute,
  private navCtrl: NavController   ) {
    this.headers = new HttpHeaders({'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT',
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
    });
    this.menteeDados.push({first_name: '',
    last_name: '',
    city:'',
    state:'',
    financial_aid:''
    })
    this.todo = this.formBuilder.group({});
    this.menteeId = this.route.snapshot.paramMap.get('id');
    this.getInformation();
    /*this.getMentee.get(`${this.API_URL}/mentees`).subscribe(data => {
      this.todo.value.username = data["objects"][0].username
      console.log(this.todo.value.username)
        //"username": data["objects"][0].username,

      //this.menteeProfile.push(data['heroesUrl']),
      //this.menteeProfile.push(data['textfile'])
        console.log(data['_body']);
       }, error => {
        console.log(error);
      });*/
  }

  public getInformation(){
    this.menteeService.getCollegeList(this.menteeId).subscribe(mentee=>{
      this.menteeDados = {
        first_name: mentee.first_name,
        last_name: mentee.last_name,
        city: mentee.city,
        state: mentee.state,
        financial_aid: mentee.financial_aid,
        universities: mentee.universities
      };
    });
  }

  public logForm(){
    console.log(this.menteeDados)
    //console.log(this.http.post(`${this.API_URL}/mentees/` + this.menteeId, this.todo.value, {headers: this.headers}))
    console.log('ˆˆ')
    
    this.http.put(`${this.API_URL}/mentees/` + this.menteeId, {
      "first_name": this.menteeDados.first_name,
      "last_name": this.menteeDados.last_name,
      "city": this.menteeDados.city,
      "state": this.menteeDados.state,
      //"email": this.todo.value.email
      "financial_aid": this.menteeDados.financial_aid,
      "universities": this.menteeDados.universities
    }, {headers: this.headers, observe: "response"}).toPromise().then((data) => {
      if (data.status == 204) {
        // FixME - line below not compiling
        //this.navCtrl.goBack("/tabs/mentee/listing/1");
        console.log('Status 204 received');
        console.log(data);
      }
      }).catch(err=> { console.log(err) })
      /*, error => {
        console.log(error);
      });*/



    /*for (let i =0; i< this.scoresArray.length; i++){
      this.http.post(`${this.API_URL}/exams`, this.scoresArray[i], {headers: this.headers}).subscribe(data => {
          console.log(data['_body']);
         }, error => {
          console.log(error);
        });
    };*/


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
