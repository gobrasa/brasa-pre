import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router'
import { MentorService } from '../shared/mentor.service';
import { Mentor } from '../shared/mentor.model'
import { LoaderService } from '../../shared/service/loader.service'
import { AlertService } from '../../shared/service/alert.service'


@Component({
  selector: 'app-mentor-detail',
  templateUrl: './mentor-detail.page.html',
  styleUrls:  ['./mentor-detail.page.scss']
})
export class MentorDetailPage {

  mentor: Mentor;

  constructor(private route: ActivatedRoute,
              private mentorService: MentorService,
              private loaderService: LoaderService,
              private alertSerice: AlertService) { }

  ionViewWillEnter() {
    const mentorId = this.route.snapshot.paramMap.get('mentorId');

    this.loaderService.presentLoading();
    this.mentorService.getMentorById(mentorId).subscribe(
      (mentor: Mentor[]) => {
        /*
        this.mentor = mentor.map((mentor: Mentor) => {
          mentor.text = this.mentorService.replaceMentorTextLine(mentor.text);

          return mentor;
        })[0];
        */

        this.loaderService.dismissLoading();
    });
  }

  updateImage() {
    /*
    this.mentor.img = 'assets/image/DefaultMentor.png'
    */
  }

}
