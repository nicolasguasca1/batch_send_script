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

        <p><strong>October 4, 2023</strong></p>

        <p>Please find attached your most recent Suspected Artificial Streaming claims report. This report originates from Spotify and identifies the suspected artificial streams from your distributed catalog. DSPs send these monthly reports to explain royalties they are withholding, to ensure you are aware of what has been distributed under your catalog, and to make us aware as your distribution partner.</p>

        <p>We have included a file named <em>Rows_Above_1000</em> which contains all the lines that are concerning and require your immediate action among the reports contained within the attachment. </p>

        <p>If you have surpassed 1,000 on any single track, we urge you to enforce a more rigorous inspection process, to investigate, review, target and stop any actions that are triggering the activity found on the tracks in question.</p>

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


# gmail address
gmail_address = 'Nicolás Guasca'

# Subject line
subject_line_delayed_report = 'Subject: Notice of Delay Regarding your September Statement'


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
