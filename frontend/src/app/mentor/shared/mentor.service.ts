import { Injectable } from '@angular/core';
import { of as ObservableOf, Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Mentor } from './mentor.model';


@Injectable()
export class MentorService {


  private readonly HS_API_URL = 'https://brasa-pre.herokuapp.com';
  private readonly API_KEY = 'WZmY7utpbDmshO1LYNtsweImq68Rp1h8e1Zjsnz63RbxE029tN';
  private headers: HttpHeaders;


  constructor(private http: HttpClient) {}


  public getAllmentorsDecks(): Observable<any>{
    return this.http.get<any>(`${this.HS_API_URL}/mentors/`);
  }


}
