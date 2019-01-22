import { Injectable } from '@angular/core';
import { of as ObservableOf, Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Mentee } from './mentee.model';


@Injectable()
export class MenteeService {

  private readonly HS_API_URL = 'https://omgvamp-hearthstone-v1.p.mashape.com';
  private readonly API_KEY = 'WZmY7utpbDmshO1LYNtsweImq68Rp1h8e1Zjsnz63RbxE029tN';
  private headers: HttpHeaders;

  constructor(private http: HttpClient) {
    //this.headers = new HttpHeaders({'X-Mashape-Key': this.API_KEY});
  }
  /*
  public replacementeeTextLine(text: string) {
    return text ? text.replace(new RegExp("\\\\n", "g"), " ") : 'No Description';
  }

  public getAllmenteeDecks(): Observable<menteeDeck[]>{


    return this.http.get<menteeDeck[]>(`${this.HS_API_URL}/info`, {headers: this.headers});

  }


  public getmenteesByDeck(menteeDeckGroup:string, menteeDeck:string): Observable<mentee[]>{

    return this.http.get<mentee[]>(`${this.HS_API_URL}/mentees/${menteeDeckGroup}/${menteeDeck}`, {headers: this.headers});

  }
  */
  public getMenteeById(menteeId:string): Observable<Mentee[]>{

    return this.http.get<Mentee[]>(`${this.HS_API_URL}/mentees/${menteeId}`, {headers: this.headers});

  }

}
