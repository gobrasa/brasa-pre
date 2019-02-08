import { Injectable } from '@angular/core';
import { of as ObservableOf, Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Mentee } from './mentee.model';


@Injectable()
export class MenteeService {


  private readonly HS_API_URL = 'http://brasa-pre.herokuapp.com';
  private readonly API_KEY = 'WZmY7utpbDmshO1LYNtsweImq68Rp1h8e1Zjsnz63RbxE029tN';
  private headers: HttpHeaders;


  constructor(private http: HttpClient) {}


  public getAllmenteeDecks(): Observable<any>{
    return this.http.get<any>(`${this.HS_API_URL}/mentees/`);
  }

  public getCollegeList(id): Observable<any>{
    return this.http.get<any>(`${this.HS_API_URL}/mentees/` + id);
  }

  public getAllExams(): Observable<any>{
    return this.http.get<any>(`${this.HS_API_URL}/exams/`);
  }

  public getAllUniversities(): Observable<any>{
    return this.http.get<any>(`${this.HS_API_URL}/universities/`);
  }






  // public getMenteeById(id: number): Observable<any>{

  // }
}
