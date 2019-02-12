import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Http, Headers } from '@angular/http'
import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router'
import { MenteeService } from '../shared/mentee.service';
import { Exam } from '../shared/exam.model';
import { Category } from '../shared/category.model';
import { LoaderService } from '../../shared/service/loader.service'
import { AlertService } from '../../shared/service/alert.service'
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import {Validators, FormBuilder, FormGroup, FormControl } from '@angular/forms';
import { IonicSelectableModule } from 'ionic-selectable';

@Component({
  selector: 'app-mentee-test',
  templateUrl: './mentee-test.page.html',
  styleUrls:  ['./mentee-test.page.scss']
})
export class MenteeTestPage {
  private todo : FormGroup;
  private readonly API_URL = 'http://brasa-pre.herokuapp.com';
  public scoresArray:any=[];
  private headers: HttpHeaders;
  public categories: Exam[];
  public subCategories: Exam[];
  form: FormGroup;
  port8Control: FormControl;
  ports10Page = 2;
  public category : Exam;
  public subCategory: Exam;
  public score: any;
  public myDate:any = Date();
  public menteeId:any;

 AddScore(){
   this.scoresArray.push({'category':'','subCategory':'', 'score': ''});
 };
 RemoveScore(idx){
   this.scoresArray.splice(idx, 1);
 };


  constructor( private formBuilder: FormBuilder,
               private http: HttpClient,
               private getMentee: HttpClient,
               private menteeService: MenteeService,
             private route: ActivatedRoute ) {
    this.headers = new HttpHeaders({'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT',
    "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept"
    });
    this.todo = this.formBuilder.group({});
    this.getExams();
    this.menteeId = this.route.snapshot.paramMap.get('id');
    console.log(this.category)
  }
  public logForm(){
console.log(this.categories)
    this.menteeService.getAllExams().subscribe(tests => {
      tests.forEach(prova=>{
        //console.log(prova.category,this.category.category)
        //console.log(prova.subcategory, this.subCategory.subcategory)
        if (prova.category == this.category.category && prova.subcategory == this.subCategory.subcategory) {
          var provaId = prova.id

          this.http.post(`${this.API_URL}/exam_schedules/`,
            {
              "realization_date": this.myDate,
                "mentee_id": this.menteeId,
                "exam_id": provaId,
                "score": this.score
            },
            {headers: this.headers}).subscribe(data => {
              console.log(data['_body']);
             }, error => {
              console.log(error);
            });

            this.getExams();
            delete this.category
            delete this.subCategory
          this.score = ''
          this.myDate = ''
        }
      })
    });
/*
    for (let i =0; i< this.scoresArray.length; i++){
      this.http.post(`${this.API_URL}/exams`, this.scoresArray[i], {headers: this.headers}).subscribe(data => {
          console.log(data['_body']);
         }, error => {
          console.log(error);
        });
    };*/


  };


  private getExams() {
   this.menteeService.getAllExams().subscribe(tests => {


     this.categories = tests
     this.subCategories = tests
     const resultCategory = [];
     const resultSubCategory = [];
     const mapCategory = new Map();
     const mapSubCategory = new Map();
     for (const item of tests) {
         if(!mapCategory.has(item.category)){
             mapCategory.set(item.category, item.category);    // set any value to Map
             resultCategory.push({
                 category: item.category
             });
             console.log(mapCategory)
         };
         if(!mapSubCategory.has(item.subcategory)){
             mapSubCategory.set(item.subcategory, item.subcategory);    // set any value to Map
             resultSubCategory.push({
                 subcategory: item.subcategory
             });
         }
       };
       this.categories = resultCategory
       this.subCategories = resultSubCategory
     /*
     tests.forEach((element)=>{
       console.log(element)
       console.log(element.category)

       this.categories.push({categoryValue: element.category})
       console.log(this.categories, '11')
     })*/
   });
 }

 public getSubcategories(categorySent) {
   console.log(categorySent.value.category)
   this.menteeService.getAllExams().subscribe(tests => {
     console.log(tests)
     this.subCategories = tests
     const resultSubCategory = [];
     const mapSubCategory = new Map();
     for (const item of tests) {
       console.log(item.category)
       if (item.category == categorySent.value.category){
         if(!mapSubCategory.has(item.subcategory)){
             mapSubCategory.set(item.subcategory, item.subcategory);    // set any value to Map
             resultSubCategory.push({
                 subcategory: item.subcategory
             });
         }
       }

       };
       this.subCategories = resultSubCategory
     /*
     tests.forEach((element)=>{
       console.log(element)
       console.log(element.category)

       this.categories.push({categoryValue: element.category})
       console.log(this.categories, '11')
     })*/
   });
 };

 /*portChange(event: { component: SelectSearchableComponent, value: any }) {
    console.log('port:', event.value);
  }*/


}
