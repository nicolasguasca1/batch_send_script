"""
Adjust the contents of the message and other parameters used by the API
"""

import os

# # Set up the email message
# txt_message = '\033[1m'+'August 11, 2023'+'\033[0m'+'\n\nDear customer, \n\nPlease find attached your most recent Suspected Artificial Streaming claims report. This report originates from Spotify and identifies the suspected artificial streams from your distributed catalog. DSPs send these monthly reports to explain royalties they are withholding, and to ensure you are aware of what has been distributed under your catalog, and to make us aware as your distribution partner.\n\nReview the attached suspected Artificial Streaming report and check our guide on How to manage artificial streaming: [https://helpdesk.revelator.com/support/solutions/articles/69000826948-how-to-manage-and-avoid-artificial-streaming] to understand if you need to take further action on the assets listed.\n\nIf none of your assets have surpassed the 1,000 artificial streams threshold, you are not being asked to take further action as your account is not at risk in any way.\n\nIf you have surpassed 1,000 on any single track, we urge you to enforce a rigorous inspection process on all tracks you distribute, to investigate and review the tracks in question, and to thoroughly read and review Revelator\'s Anti Fraud Policy: [https://www.revelator.com/anti-fraud-policy].\n\nDistributing Artificial Streaming is regarded as fraud by our DSP partners and poses a risk to all of us. Understanding your responsibilities in combating music fraud as a Revelator customer is vital.\n\nDo you require our assistance in creating or implementing an anti-fraud policy? Are you in need of help in tracking inspections? If so, please book a time with me here: [https://pages.revelator.com/meetings/nicolas-guasca/customer-success].\n\nLet\'s discuss how we can offer support.\n\nAppreciate your attention to this matter,\n\nNicolás Guasca\nCustomer Success Manager'

txt_message_above = '''<!DOCTYPE html >
<html >
<head >
   <style >
      body {{
           font-family: Arial, sans-serif
           }}
    </style >
</head >
<body >
    <div>
        <p>Dear Customer,</p>

        <p><strong>Jan 11, 2024</strong></p>

        <p>Please find attached your most recent Suspected Artificial Streaming claims report. This report contains files originated by Spotify. It identifies the suspected artificial streams from your distributed catalog. DSPs send these monthly reports to explain royalties they are withholding, to ensure you are aware of what has been distributed under your catalog, and to make us aware as your distribution partner.</p>

        <p>We have included files with the naming convention <em>Rows_Above_</em> which contains all the lines that are concerning and require your immediate action among the reports contained within the attachment. </p>

        <p>For any single track referenced, we urge you to enforce a more rigorous inspection process, to investigate, review, target and stop any actions that are triggering the activity found on the tracks in question.</p>

        <p>Check our guide on <a href="https://helpdesk.revelator.com/support/solutions/articles/69000826948-how-to-manage-and-avoid-artificial-streaming" target="blank">How to Manage Artificial Streaming</a> for additional information.</p>

        <p>Distributing Artificial Streaming is regarded as fraud by our DSP partners and poses a risk to all of us. Understanding your responsibilities in combating music fraud as a Revelator customer is vital.</p>

        <p>Do you require our assistance in creating or implementing an anti-fraud policy? Are you in need of help in tracking inspections? If so, please <a href="https://pages.revelator.com/meetings/nicolas-guasca/customer-success" target="blank">book a time with me here</a> and let's discuss how we can offer support.</p>

        <p> Appreciate your attention to this matter.</p>

        <p>Nicolás Guasca</p>

            <p>&nbsp;</p>
        <h3 style="text-align: center; color: #3f7320;"><span class="gmail_signature_prefix">--</span></h3>
        <div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature">
            <div dir="ltr">
                <div>Nicol&aacute;s Guasca Santamar&iacute;a</div>
                <div>Customer Success<i><br /></i></div>
                <div><i>&nbsp;</i></div>
                <div><i>Music's Everything<br /></i></div>
                <div><i><u>Revelator.com</u></i></div>
                <div><i><u>&nbsp;</u></i></div>
                <div>
                    <div dir="ltr"><img src="https://ci6.googleusercontent.com/proxy/18AqzZnGrP1Wpvy-RSmi0kuXheOQpQ_mps8LqW5ZMbfx8oUrEykUfwgrR2vmmS3U5N_DfHm7tCpkf4FJeHxJHfv3FU1QP1oK7aNAU62xiLD9t4_wpdCRzP_iHdxRroivj3upVuC0mpIj=s0-d-e1-ft#https://files.constantcontact.com/df90a1cb001/6be6a782-2469-4743-b2f7-ebc61623d361.png" width="96" height="13" class="CToWUd" data-bit="iit" /></div>
                    <div dir="ltr"><b><span style="color: #000000;">Recently featured on</span><span style="color: #500050;">&nbsp;</span></b><a href="https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw3GSD26HNjpRsrlJ1gVZqtQ" rel="noopener">interdependence</a><span>&nbsp;|&nbsp;</span><a href="https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign=Investor%20Outreach&amp;utm_source=Music%20Business%20Worldwide:%20Decentralization&amp;utm_medium=Music%20Business%20Worldwide:%20Decentralization" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign%3DInvestor%2520Outreach%26utm_source%3DMusic%2520Business%2520Worldwide:%2520Decentralization%26utm_medium%3DMusic%2520Business%2520Worldwide:%2520Decentralization&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw0Zk2M7-_6ZByVFnycq4Y-5" rel="noopener">Music Business Worldwide</a></div>
                    <div dir="ltr"></div>
                    <div dir="ltr"><span style="color: #999999; font-size: xx-small;">CONFIDENTIALITY NOTICE: This message (including any attachments) is intended only for the use of the individual or entity to which it is addressed and may contain materials protected by copyright or information that is non-public, proprietary, privileged, confidential, and exempt from disclosure under applicable law or agreement. If you are not the intended recipient, you are hereby notified that any review use, dissemination, distribution, or duplication of this communication is strictly prohibited. If you are not the intended recipient, please contact the sender immediately by reply email and destroy all copies of the original. Thank you.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body >
</html >
'''

txt_message_below = '''<!DOCTYPE html >
<html >
<head >
   <style >
      body {{
           font-family: Arial, sans-serif
           }}
    </style >
</head >
<body >
    <div>
        <p>Dear Partner,</p>

        <p><strong>October 4, 2023</strong></p>

        <p>Attached is the most recent Suspected Artificial Streaming report we received from Spotify regarding your content. Spotify sends these reports to explain royalties they withhold and to provide you with an opportunity to identify any growing momentum of fraudulent activity within your catalog.</p>

        <p><strong>Important: Receiving this email doesn’t indicate fraud in your account!</strong></p>

        <p>We forward these reports exactly as received from the DSP, so you can review them, take prompt action if needed, and prevent potential permanent content removal in the future.</p>

        <p>The attached suspected report is for informational purposes. Feel free to check our guide on <a href="https://helpdesk.revelator.com/support/solutions/articles/69000826948-how-to-manage-and-avoid-artificial-streaming" target="blank">How to Manage Artificial Streaming</a> to understand typical warning signs on your assets.</p>

        <p>As none of your assets have surpassed the 1,000 artificial streams threshold, you are not being asked by Revelator to take further action, and your account is not at risk in any way.</p>

        <p>Should you have any other questions regarding Artificial Streams, don’t hesitate to write to us at infringement@revelator.com. We’re always available to assist and advise.</p>

        <p> Appreciate your partnership</p>

        <p>Nicolás Guasca</p>

            <p>&nbsp;</p>
        <h3 style="text-align: center; color: #3f7320;"><span class="gmail_signature_prefix">--</span></h3>
        <div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature">
            <div dir="ltr">
                <div>Nicol&aacute;s Guasca Santamar&iacute;a</div>
                <div>Customer Success<i><br /></i></div>
                <div><i>&nbsp;</i></div>
                <div><i>Music's Everything<br /></i></div>
                <div><i><u>Revelator.com</u></i></div>
                <div><i><u>&nbsp;</u></i></div>
                <div>
                    <div dir="ltr"><img src="https://ci6.googleusercontent.com/proxy/18AqzZnGrP1Wpvy-RSmi0kuXheOQpQ_mps8LqW5ZMbfx8oUrEykUfwgrR2vmmS3U5N_DfHm7tCpkf4FJeHxJHfv3FU1QP1oK7aNAU62xiLD9t4_wpdCRzP_iHdxRroivj3upVuC0mpIj=s0-d-e1-ft#https://files.constantcontact.com/df90a1cb001/6be6a782-2469-4743-b2f7-ebc61623d361.png" width="96" height="13" class="CToWUd" data-bit="iit" /></div>
                    <div dir="ltr"><b><span style="color: #000000;">Recently featured on</span><span style="color: #500050;">&nbsp;</span></b><a href="https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw3GSD26HNjpRsrlJ1gVZqtQ" rel="noopener">interdependence</a><span>&nbsp;|&nbsp;</span><a href="https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign=Investor%20Outreach&amp;utm_source=Music%20Business%20Worldwide:%20Decentralization&amp;utm_medium=Music%20Business%20Worldwide:%20Decentralization" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign%3DInvestor%2520Outreach%26utm_source%3DMusic%2520Business%2520Worldwide:%2520Decentralization%26utm_medium%3DMusic%2520Business%2520Worldwide:%2520Decentralization&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw0Zk2M7-_6ZByVFnycq4Y-5" rel="noopener">Music Business Worldwide</a></div>
                    <div dir="ltr"></div>
                    <div dir="ltr"><span style="color: #999999; font-size: xx-small;">CONFIDENTIALITY NOTICE: This message (including any attachments) is intended only for the use of the individual or entity to which it is addressed and may contain materials protected by copyright or information that is non-public, proprietary, privileged, confidential, and exempt from disclosure under applicable law or agreement. If you are not the intended recipient, you are hereby notified that any review use, dissemination, distribution, or duplication of this communication is strictly prohibited. If you are not the intended recipient, please contact the sender immediately by reply email and destroy all copies of the original. Thank you.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body >
</html >
'''

txt_message_royalties_delayed = '''<!DOCTYPE html >
<html >
<head >
   <style >
      body {{
           font-family: Arial, sans-serif
           }}
      p {{
        margin-bottom: 10px; /* Adds margin below each <p> element */
    }}
    </style >
</head >
<body >
    <div>
        <p>Hello {company_name} team,</p><br>

        <p>As we value our partnership and strive to maintain transparency in all our interactions, I wanted to inform you that your monthly royalty statement from Revelator will be slightly delayed.</p>
        
        <p>The reason for this delay is that we are currently conducting a thorough platform review of all content, including filtering out fraudulent releases and artificial streaming activities and your account requires manual inspection and review. This additional review is essential for the long-term success of our collaboration.</p>

        <p>We're working hard to make our review process faster and to ensure that your payment has the shortest delay possible. Your active participation in thorough inspection and catalog review will help ensure this process can be faster in the future.</p>

        <p>We'll let you know as soon as the statements are approved and ready for your review.</p>

        <p>Thanks for your continued trust and partnership. If you have any questions or concerns, please don’t hesitate to reach out to us. We're here to assist as always.</p><br>

        <p> Best regards,</p>

        <p>Nicolás Guasca</p>

            <p>&nbsp;</p>
        <h3 style="text-align: center; color: #3f7320;"><span class="gmail_signature_prefix">--</span></h3>
        <div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature">
            <div dir="ltr">
                <div>Nicol&aacute;s Guasca Santamar&iacute;a</div>
                <div>Customer Success<i><br /></i></div>
                <div><i>&nbsp;</i></div>
                <div><i>Music's Everything<br /></i></div>
                <div><i><u>Revelator.com</u></i></div>
                <div><i><u>&nbsp;</u></i></div>
                <div>
                    <div dir="ltr"><img src="https://ci6.googleusercontent.com/proxy/18AqzZnGrP1Wpvy-RSmi0kuXheOQpQ_mps8LqW5ZMbfx8oUrEykUfwgrR2vmmS3U5N_DfHm7tCpkf4FJeHxJHfv3FU1QP1oK7aNAU62xiLD9t4_wpdCRzP_iHdxRroivj3upVuC0mpIj=s0-d-e1-ft#https://files.constantcontact.com/df90a1cb001/6be6a782-2469-4743-b2f7-ebc61623d361.png" width="96" height="13" class="CToWUd" data-bit="iit" /></div>
                    <div dir="ltr"><b><span style="color: #000000;">Recently featured on</span><span style="color: #500050;">&nbsp;</span></b><a href="https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw3GSD26HNjpRsrlJ1gVZqtQ" rel="noopener">interdependence</a><span>&nbsp;|&nbsp;</span><a href="https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign=Investor%20Outreach&amp;utm_source=Music%20Business%20Worldwide:%20Decentralization&amp;utm_medium=Music%20Business%20Worldwide:%20Decentralization" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign%3DInvestor%2520Outreach%26utm_source%3DMusic%2520Business%2520Worldwide:%2520Decentralization%26utm_medium%3DMusic%2520Business%2520Worldwide:%2520Decentralization&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw0Zk2M7-_6ZByVFnycq4Y-5" rel="noopener">Music Business Worldwide</a></div>
                    <div dir="ltr"></div>
                    <div dir="ltr"><span style="color: #999999; font-size: xx-small;">CONFIDENTIALITY NOTICE: This message (including any attachments) is intended only for the use of the individual or entity to which it is addressed and may contain materials protected by copyright or information that is non-public, proprietary, privileged, confidential, and exempt from disclosure under applicable law or agreement. If you are not the intended recipient, you are hereby notified that any review use, dissemination, distribution, or duplication of this communication is strictly prohibited. If you are not the intended recipient, please contact the sender immediately by reply email and destroy all copies of the original. Thank you.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body >
</html >
'''

# Sent Aug 7th, 2024
txt_message_Spotify = '''<!DOCTYPE html >
<html >
<head >
   <style >
      body {{
           font-family: Arial, sans-serif
           }}
    </style >
</head >
<body >
    <div>
        <p>Dear Partner,</p>

        <p><strong>Aug 31st, 2024</strong></p>

        <p>Please find attached the latest data from Spotify regarding all artificial streaming (AS) related to your catalog.</p>

        <p>1. This email contains a report of AS that Spotify has identified for <strong>July 2024</strong> streaming activity.</p>

        <p>2. If applicable, this email will also contain a report for tracks fined by Spotify for excessive AS resulting from <strong>June 2024</strong> streaming activity. If no such report is attached to this email this means that your catalog has not been fined at this time.</p>

        <p>Please note:</p>

        <ul>
        <li>
            <p>As a result of Spotify’s new fine policy and their slow reporting schedule, Revelator is working on a system to identify potential Spotify AS on a daily basis in order to protect you from being abused by bad actors and the resulting fines. We are in the testing phases of this system and aim to release it as soon as we can ensure a high level of confidence in the tracks we identify.</p>

        </li>

        <li>
            <p>Given Spotify’s reporting schedule it is likely that tracks which were fined for previous month AS will have further incurred fines in the next months. You should consider whether to take down these tracks now to avoid the same fines for your next report.</p>
        </li>

        <li>
            <p>We strongly encourage you to reach out to your artists identified in the first report and ensure that they are not engaging in campaigns resulting in their tracks being flagged for AS. If they are, please have them cease these campaigns immediately. <strong>Note that Revelator will need to block distribution to Spotify for any artist whose catalog is repeatedly identified by Spotify to be engaging in AS.</strong> If your artist claims that this AS activity is the result of being added to a playlist against their will, then please make sure to have them report this to Spotify through their Spotify for Artist account, and to keep a record of the ISRC(s) and the related playlist URL(s). Such information will be needed if you ever want to contest Spotify’s AS reporting and/or fines.</p>
        </li>

        <li>
            <p>Lastly, we’d like to clarify the following points as pertains to Spotify’s new fine policy</p>

            <p>This penalty is meant to be applied only against the artist/rights holder of the penalized track. It is not intended to be applied across all your accounts and/or impact non-violating artists in any way.</p>

            <p>We encourage you to keep educating your clients as to the perils of stream boosting campaigns and share with them <a href="https://docs.google.com/document/d/1KuPye_-PQK3rGaqyilwnjncNQZZhde2fRe_gwD_7qgY/edit" target="blank">Spotify’s Artificial Streaming Education</a> notice.</p>

            <p>We have further added such warnings in your dashboard so that whenever one of your clients distributes a new release they are reminded of the consequences of running such stream boosting campaigns.</p>
        </li>
        </ul>
        
        <p>Should you need to follow up on this email, please be sure to add support@revelator.com in CC.</p>

        <p>Best regards,</p>

        <p>Revelator</p>

            <p>&nbsp;</p>
        <h3 style="text-align: center; color: #3f7320;"><span class="gmail_signature_prefix">--</span></h3>
        <div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature">
            <div dir="ltr">
                <div>Nicol&aacute;s Guasca Santamar&iacute;a</div>
                <div>Distribution & Operations<i><br /></i></div>
                <div><i>&nbsp;</i></div>
                <div><i>Music's Everything<br /></i></div>
                <div><i><u>Revelator.com</u></i></div>
                <div><i><u>&nbsp;</u></i></div>
                <div>
                    <div dir="ltr"><img src="https://ci6.googleusercontent.com/proxy/18AqzZnGrP1Wpvy-RSmi0kuXheOQpQ_mps8LqW5ZMbfx8oUrEykUfwgrR2vmmS3U5N_DfHm7tCpkf4FJeHxJHfv3FU1QP1oK7aNAU62xiLD9t4_wpdCRzP_iHdxRroivj3upVuC0mpIj=s0-d-e1-ft#https://files.constantcontact.com/df90a1cb001/6be6a782-2469-4743-b2f7-ebc61623d361.png" width="96" height="13" class="CToWUd" data-bit="iit" /></div>
                    <div dir="ltr"><b><span style="color: #000000;">Recently featured on</span><span style="color: #500050;">&nbsp;</span></b><a href="https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw3GSD26HNjpRsrlJ1gVZqtQ" rel="noopener">interdependence</a><span>&nbsp;|&nbsp;</span><a href="https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign=Investor%20Outreach&amp;utm_source=Music%20Business%20Worldwide:%20Decentralization&amp;utm_medium=Music%20Business%20Worldwide:%20Decentralization" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign%3DInvestor%2520Outreach%26utm_source%3DMusic%2520Business%2520Worldwide:%2520Decentralization%26utm_medium%3DMusic%2520Business%2520Worldwide:%2520Decentralization&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw0Zk2M7-_6ZByVFnycq4Y-5" rel="noopener">Music Business Worldwide</a></div>
                    <div dir="ltr"></div>
                    <div dir="ltr"><span style="color: #999999; font-size: xx-small;">CONFIDENTIALITY NOTICE: This message (including any attachments) is intended only for the use of the individual or entity to which it is addressed and may contain materials protected by copyright or information that is non-public, proprietary, privileged, confidential, and exempt from disclosure under applicable law or agreement. If you are not the intended recipient, you are hereby notified that any review use, dissemination, distribution, or duplication of this communication is strictly prohibited. If you are not the intended recipient, please contact the sender immediately by reply email and destroy all copies of the original. Thank you.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body >
</html >
'''

# Sent Aug 5th, 2024
txt_message_ALL_DSPS = '''<!DOCTYPE html >
<html >
<head >
   <style >
      body {{
           font-family: Arial, sans-serif
           }}
    </style >
</head >
<body >
    <div>
        <p>Dear Partner,</p>

        <p><strong>Aug 5th, 2024</strong></p>

        <p>In the attached reports we’ve further highlighted with “Rows_Above” the tracks with more than 1,000 AS to help you identify the worst offenders and prioritize your response. If you find 0 rows within this document, it means you have no assets reported above this threshold.</p>

        <p>Although the threshold is not a good measurement of how compromised your catalog is for DSPs like Spotify, we urge you to still carefully review this report to have a reference on the fraudulent activity from your account on this platform.</p>

        <p><strong>NEXT STEPS</strong></p>

        <ul>
        <li>
            <p>Please review the content and discuss it with your clients in order to determine whether this is the result of fraudulent behavior or the use of a playlisting/stream boosting service. Note that most of these services engage in practices which the DSPs consider to be abusive and to constitute AS. You can read more about this in this <a href="https://support.spotify.com/us/artists/article/third-party-services-that-guarantee-streams/" target="_blank">Spotify article</a>. Also, this <a href="https://artists.spotify.com/video/what-is-artificial-streaming" target="_blank">video from Spotify</a> is useful in explaining AS and educating your clients as to its harm.</p>


        </li>

        <li>
            <p>Have your clients immediately cease any activity leading to the reported AS, and notify them of the many potential consequences:</p>
            <p>a. Withholding of royalties</p>
            <p>b. Permanent removal of their track from the DSP</p>
            <p><a href="https://www.music-tomorrow.com/blog/the-negative-impact-of-fake-streams-on-artists-algorithmic-performance" target="_blank">c. Harming their overall profile and the discovery of their music</a></p>
            
        </li>

        <li>
            <p>If you suspect a bad actor, we further encourage you to take down their entire catalog and terminate their account.</p>
        </li>

        </ul>
        
        <p>We urge you to carefully monitor and review your catalog now so as to get ahead of significant potential penalties coming in the near future.</p>

        <p>If you need our assistance regarding this matter, please <a href="https://meetings.hubspot.com/maya-marija" target="_blank">book a time with our team here</a> or reply to this email and CC support@revelator.com if you have some basic questions.</p>

        <p>We appreciate your attention to this matter.</p>

        <p>Best regards,</p>

        <p>Revelator</p>

            <p>&nbsp;</p>
        <h3 style="text-align: center; color: #3f7320;"><span class="gmail_signature_prefix">--</span></h3>
        <div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature">
            <div dir="ltr">
                <div>Nicol&aacute;s Guasca Santamar&iacute;a</div>
                <div>Distribution & Operations<i><br /></i></div>
                <div><i>&nbsp;</i></div>
                <div><i>Music's Everything<br /></i></div>
                <div><i><u>Revelator.com</u></i></div>
                <div><i><u>&nbsp;</u></i></div>
                <div>
                    <div dir="ltr"><img src="https://ci6.googleusercontent.com/proxy/18AqzZnGrP1Wpvy-RSmi0kuXheOQpQ_mps8LqW5ZMbfx8oUrEykUfwgrR2vmmS3U5N_DfHm7tCpkf4FJeHxJHfv3FU1QP1oK7aNAU62xiLD9t4_wpdCRzP_iHdxRroivj3upVuC0mpIj=s0-d-e1-ft#https://files.constantcontact.com/df90a1cb001/6be6a782-2469-4743-b2f7-ebc61623d361.png" width="96" height="13" class="CToWUd" data-bit="iit" /></div>
                    <div dir="ltr"><b><span style="color: #000000;">Recently featured on</span><span style="color: #500050;">&nbsp;</span></b><a href="https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw3GSD26HNjpRsrlJ1gVZqtQ" rel="noopener">interdependence</a><span>&nbsp;|&nbsp;</span><a href="https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign=Investor%20Outreach&amp;utm_source=Music%20Business%20Worldwide:%20Decentralization&amp;utm_medium=Music%20Business%20Worldwide:%20Decentralization" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign%3DInvestor%2520Outreach%26utm_source%3DMusic%2520Business%2520Worldwide:%2520Decentralization%26utm_medium%3DMusic%2520Business%2520Worldwide:%2520Decentralization&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw0Zk2M7-_6ZByVFnycq4Y-5" rel="noopener">Music Business Worldwide</a></div>
                    <div dir="ltr"></div>
                    <div dir="ltr"><span style="color: #999999; font-size: xx-small;">CONFIDENTIALITY NOTICE: This message (including any attachments) is intended only for the use of the individual or entity to which it is addressed and may contain materials protected by copyright or information that is non-public, proprietary, privileged, confidential, and exempt from disclosure under applicable law or agreement. If you are not the intended recipient, you are hereby notified that any review use, dissemination, distribution, or duplication of this communication is strictly prohibited. If you are not the intended recipient, please contact the sender immediately by reply email and destroy all copies of the original. Thank you.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body >
</html >
'''


txt_penalty_update = '''<!DOCTYPE html >
<html >
<head >
   <style >
      body {{
           font-family: Arial, sans-serif
           }}
    </style >
</head >
<body >
    <div>
        <p>Dear Partner,</p>

        <p><strong>May 30th, 2024</strong></p>

        <p>Please find attached your April Spotify artificial streaming (AS) report, and in some cases an additional 'filtered_records' report has been added if any of your tracks had 90% or more of their streams identified as artificial by Spotify. This additional report corresponds to the tracks to which Spotify’s new 10 Euro fine is expected to apply. <strong>Do note, however, that there remains a considerable lack of clarity from Spotify as to the application of this penalty:</strong> </p>
        
        <p>1. It is unclear whether penalties will actually be applied for April streaming activity.</p>
        <p>2. It is also unclear whether these penalties will be applied for May streaming activity. Please note that our penalty report is based on April activity and that Spotify has not yet provided their May AS report for us to identify if the same tracks that would be penalized for April would also be penalized for May. Nevertheless, we prefer to provide you with this information now so that you can either take down all such tracks now to avoid potential penalties for June, or urgently reach out to your clients to have them stop all activities which may have resulted in Spotify flagging their tracks as having a high amount of AS.</p>
        <p>3. We will provide you with our May penalty report as soon as possible, but we do not expect to receive the information from Spotify before the last week of June.</p>
        <p>4. Your Penalty report may have more than 1 row with the same ISRC. If that is the case, you should expect to be fined only 1 time: we indicated all the releases with the ISRC to make it easier to identify which releases to take down from Spotify if you wish to remove this content.</p>

        <p>In addition, we’d like to clarify the following points as pertains to Spotify’s new policy:</p>

        <p>1. Along with the rest of our fellow distributors we have repeatedly communicated to Spotify that their new policy is problematic — all the more so based on their delayed AS reporting schedule which can result in the same track being fined for 2 months before you are made aware of its high amount of AS. We regret to say that despite all this feedback from distributors across the industry Spotify has decided to maintain its new penalty policy.</p>

        <p>2. This penalty is meant to be applied only against the artist/rights holder of the penalized track. It is not intended to be applied across all your accounts and/or impact non-violating artists in any way.</p>

        <p>3. We encourage you to keep educating your clients as to the perils of stream boosting campaigns and share with them <a href="https://docs.google.com/document/d/1KuPye_-PQK3rGaqyilwnjncNQZZhde2fRe_gwD_7qgY/edit" target="blank">Spotify’s Artificial Streaming Education information. </a></p>

        <p>4. We have further added such warnings in your dashboard so that whenever one of your clients distributes a new release they are reminded of the consequences of running such stream boosting campaigns.</p>

        <p>We will update you as soon as Spotify provides further clarity on the application of their new policy. Remember to reply with support@revelator.com in cc to open a case for this matter.</p>

        <p>Best regards,</p>

        <p>Revelator</p>

            <p>&nbsp;</p>
        <h3 style="text-align: center; color: #3f7320;"><span class="gmail_signature_prefix">--</span></h3>
        <div dir="ltr" class="gmail_signature" data-smartmail="gmail_signature">
            <div dir="ltr">
                <div>Nicol&aacute;s Guasca Santamar&iacute;a</div>
                <div>Distribution & Operations<i><br /></i></div>
                <div><i>&nbsp;</i></div>
                <div><i>Music's Everything<br /></i></div>
                <div><i><u>Revelator.com</u></i></div>
                <div><i><u>&nbsp;</u></i></div>
                <div>
                    <div dir="ltr"><img src="https://ci6.googleusercontent.com/proxy/18AqzZnGrP1Wpvy-RSmi0kuXheOQpQ_mps8LqW5ZMbfx8oUrEykUfwgrR2vmmS3U5N_DfHm7tCpkf4FJeHxJHfv3FU1QP1oK7aNAU62xiLD9t4_wpdCRzP_iHdxRroivj3upVuC0mpIj=s0-d-e1-ft#https://files.constantcontact.com/df90a1cb001/6be6a782-2469-4743-b2f7-ebc61623d361.png" width="96" height="13" class="CToWUd" data-bit="iit" /></div>
                    <div dir="ltr"><b><span style="color: #000000;">Recently featured on</span><span style="color: #500050;">&nbsp;</span></b><a href="https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://interdependence.fm/episodes/bringing-the-music-industry-on-chain-with-bruno-guez-revelator&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw3GSD26HNjpRsrlJ1gVZqtQ" rel="noopener">interdependence</a><span>&nbsp;|&nbsp;</span><a href="https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign=Investor%20Outreach&amp;utm_source=Music%20Business%20Worldwide:%20Decentralization&amp;utm_medium=Music%20Business%20Worldwide:%20Decentralization" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.musicbusinessworldwide.com/what-would-it-really-take-to-decentralize-the-music-industry/?utm_campaign%3DInvestor%2520Outreach%26utm_source%3DMusic%2520Business%2520Worldwide:%2520Decentralization%26utm_medium%3DMusic%2520Business%2520Worldwide:%2520Decentralization&amp;source=gmail&amp;ust=1691790766677000&amp;usg=AOvVaw0Zk2M7-_6ZByVFnycq4Y-5" rel="noopener">Music Business Worldwide</a></div>
                    <div dir="ltr"></div>
                    <div dir="ltr"><span style="color: #999999; font-size: xx-small;">CONFIDENTIALITY NOTICE: This message (including any attachments) is intended only for the use of the individual or entity to which it is addressed and may contain materials protected by copyright or information that is non-public, proprietary, privileged, confidential, and exempt from disclosure under applicable law or agreement. If you are not the intended recipient, you are hereby notified that any review use, dissemination, distribution, or duplication of this communication is strictly prohibited. If you are not the intended recipient, please contact the sender immediately by reply email and destroy all copies of the original. Thank you.</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body >
</html >
'''

txt_violative_content = '''<!DOCTYPE html >
<html >
<head >
   <style >
      body {{
           font-family: Arial, sans-serif;
           }}
    </style >
</head >
<body >
    <div>
        <p>Dear Partner,</p>

        <p>TikTok has identified the following content from your catalog as potentially invalid for TikTok (and all other UGC DSPs: Facebook Rights Manager, Snap, and YouTube CID).</p>
        
        <p>Please review the content and ensure that it is appropriate for <a href="https://helpdesk.revelator.com/a/solutions/articles/69000828338" target="blank">UGC DSPs </a> (and note that TikTok has further provided a reason why the content may be inappropriate).</p>
        
        <p><strong>Deadline for responding: Monday, August 19, 13:00 GMT.</strong> Please note that if we do not receive a response from you by that time, we will consider the content to be violative and take it down from all appropriate DSPs (in some cases all DSPs if the content requires a license).</p>
        
        <p>If the content is indeed inappropriate:</p>
        <ul>
            <li>Please remove the content from all relevant DSPs:</li>
            <ul>
                <li>All DSPs when the TikTok Issue is:
                    <ul>
                        <li>Ineligible Delivery</li>
                        <li>Potentially Invalid</li>
                        <li>Sped Up/Slowed Down</li>
                        <li>Viral Mix/Mashup — or possibly only UGC DSPs, depending on the license(s) provided</li>
                    </ul>
                </li>
                <li>UGC DSPs when the TikTok Issue is:
                    <ul>
                        <li>Hidden Recording</li>
                        <li>UGC/PGC Copycat</li>
                        <li>Viral Mix/Mashup — or possibly all DSPs, depending on the license(s) provided</li>
                    </ul>
                </li>
            </ul>
        </ul>
        
        <p>Please email us back to indicate your actions for each UPC.</p>

        <p>If you contest TikTok’s findings and the content is indeed appropriate:</p>
        <ul>
            <li>Please email us back indicating the UPC and the reason why this content does not violate TikTok’s Content Policy.</li>
            <li>If the content derives from, or includes, 3rd party content, please also attach all related license document(s).</li>
        </ul>

        <p>Thank you and all the best,</p>
        
        <p>Revelator</p>
    </div>
</body >
</html >
'''



# gmail address
gmail_address = 'Nicolás Guasca'

# Subject lines
subject_line_delayed_report = 'Subject: Notice of Delay Regarding your November Statement'

subject_line_above = 'Spotify AS Report August: Action Required'

subject_line_below = 'Spotify AS Report August: No Action Required'

subject_line_all = 'Spotify Artificial Streaming Reports 07/2024'

subject_line_VIOLATIVE = '🔥 YOUR ACTION NEEDED - TikTok Invalid Content'


# subject = : <span>&#x1F525;</span> URGENT - Spotify Artificial Streaming Report and Potential Fines


# The gmail API can be used to send emails
scopes = ['https://www.googleapis.com/auth/gmail.send']

# Path to the credenciales file
credenciales = 'credenciales.json'
# Check that the credenciales file exists
assert os.path.exists(
    credenciales), f"credenciales file {credenciales} does not exist"

# Port
port = 0

# Maximum number of emails to send before pause (see https://developers.google.com/gmail/api/reference/quota)
max_emails = 100
