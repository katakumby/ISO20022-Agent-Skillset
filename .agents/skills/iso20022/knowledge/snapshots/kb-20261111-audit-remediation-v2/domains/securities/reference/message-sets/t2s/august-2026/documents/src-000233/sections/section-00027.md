---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["3 admi.006.001.01 ResendRequestV01", "3.4 Message Building Blocks", "3.4.2 ResendSearchCriteria <RsndSchCrit>", "3.4.2.1 BusinessDate <BizDt>"]
file_pages: [59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.006.001.01"]
---

# 3.4.2.1 BusinessDate <BizDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 59 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 59

```text
ResendSearchCriteria <RsndSchCrit> contains the following ResendSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BusinessDate <BizDt> [0..1] Date 59
   SequenceNumber <SeqNb> [0..1] Text 59
   SequenceRange <SeqRg> [0..1] ± 59
   OriginalMessageNameIdentification <OrgnlMsgNmId> [0..1] Text 60
   FileReference <FileRef> [0..1] Text 60
   Recipient <Rcpt> [1..1] ± 60
3.4.2.1  BusinessDate <BizDt>
Presence: [0..1]
Definition: Date of the business day of the requested messages the resend function is used for.
Datatype: "ISODate" on page 3319
3.4.2.2  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Independent counter for message sequence, which is available once per party technical
address.
Specifies the identification sequence number for a specific couple sender/receiver.
Datatype: "Max35Text" on page 3328
3.4.2.3  SequenceRange <SeqRg>
Presence: [0..1]
Definition: Independent counter for a range of message sequences, which are available once per party
technical address.
Specifies the range of identification sequence numbers for a specific couple sender/receiver.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.006.001.01 ResendRequestV01
Target2-Securities 59 August 2026
```

