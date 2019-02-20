import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-card-list',
  templateUrl: './mentee-list.component.html'
})

export class MenteeListComponent {
  @Input() items: any[] = [];
  @Input() listName: string;
}
