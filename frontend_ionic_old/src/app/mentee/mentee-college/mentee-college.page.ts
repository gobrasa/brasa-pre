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
import { University } from '../shared/university';


@Component({
  selector: 'app-mentee-college',
  templateUrl: './mentee-college.page.html',
  styleUrls:  ['./mentee-college.page.scss']
})
export class MenteeCollegePage {
  //private todo : FormGroup;
  private readonly API_URL = 'http://brasa-pre.herokuapp.com';
  //public collegeArray:any=[];
  private headers: HttpHeaders;
  public universities: University[];
  //form: FormGroup;
  //port8Control: FormControl;
  //ports10Page = 2;
  //public category : University;
  menteeId: any;
  public selectedUnis: University[]=[];

 /*AddCollege(){
   this.collegeArray.push({'':''});
 };
 RemoveCollege(idx){
   this.collegeArray.splice(idx, 1);
 };*/

  constructor( private formBuilder: FormBuilder,
    private http: HttpClient,
    private getMentee: HttpClient,
    private menteeService: MenteeService,
  private route: ActivatedRoute ) {
    this.headers = new HttpHeaders({'Content-Type': 'application/json',
    "accept": "application/json"
    });
    //this.collegeArray.push({'link':''});
    //this.todo = this.formBuilder.group({});
    this.getUniList();
    this.menteeId = this.route.snapshot.paramMap.get('id');
    this.selectColleges(this.menteeId);

  }

  public postCollegeList(collegeList){
    const universitiesId = [];
    collegeList.value.forEach(test=>{
      universitiesId.push(test.id)
    })

    this.http.post(`${this.API_URL}/university_applications/university_applications_mentee/` + this.menteeId,
      {universities: universitiesId},
      {headers: this.headers}).subscribe(data => {
        console.log(data['_body']);
       }, error => {
        console.log(error);
      });
  };

  public selectColleges(id){
    this.menteeService.getCollegeList(id).subscribe(tests=>{
      tests.university_applications.forEach(unis=>{
        this.selectedUnis.push({id: unis.university.id, name:  unis.university.name})
      })
    })
  };

  /*public logForm(){
    for (let i =0; i< this.collegeArray.length; i++){
      this.http.post(`${this.API_URL}/universities/`, this.collegeArray[i], {headers: this.headers}).subscribe(data => {
          console.log(data['_body']);
         }, error => {
          console.log(error);
        });
    };
  };*/

  private getUniList() {
   this.menteeService.getAllUniversities().subscribe(tests => {
     this.universities = tests
     const result = [];
     const mapUniversities = new Map();
     for (const item of tests) {
         if(!mapUniversities.has(item.name)){
             mapUniversities.set(item.name, item.name);    // set any value to Map
             result.push({
                  id: item.id,
                 name: item.name
             });
         };

       };
       this.universities = result

   });
 }

}
