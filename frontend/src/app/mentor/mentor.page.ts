import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-mentor',
  templateUrl: './mentor.page.html',
  styleUrls: ['./mentor.page.scss'],
})
export class MentorPage implements OnInit {

  private selectedItem: any;
  private icons = [
    'flask',
    'wifi',
    'beer',
    'football',
    'basketball',
    'paper-plane',
    'american-football',
    'boat',
    'bluetooth',
    'build'
  ];
  public items: Array<{ title: string; note: string; icon: string }> = [];
  

  constructor() {
    for (let i = 1; i < 11; i++) {
      this.items.push({
        title: 'Mentor ' + i,
        note: 'Note #' + i,
        icon: this.icons[Math.floor(Math.random() * this.icons.length)]
      });
    }
   }

  ngOnInit() {
  }

}
