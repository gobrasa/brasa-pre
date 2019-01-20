import { Component } from '@angular/core';
import {Validators, FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  private todo : FormGroup;

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

  constructor( private formBuilder: FormBuilder ) {
    this.todo = this.formBuilder.group({
      title: ['', Validators.required],
      description: [''],
    });
  }
  logForm(){
    console.log(this.todo.value)
  }
}
