---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 admi.006.001.01 ResendRequestV01", "3.4 Message Building Blocks", "3.4.2 ResendSearchCriteria <RsndSchCrit>", "3.4.2.1 BusinessDate <BizDt>"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.006.001.01"]
---

# 3.4.2.1 BusinessDate <BizDt>

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
ResendSearchCriteria <RsndSchCrit> contains the following ResendSearchCriteria2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BusinessDate <BizDt> [0..1] Date 29
   SequenceNumber <SeqNb> [0..1] Text 29
   SequenceRange <SeqRg> [0..1] ± 29
   OriginalMessageNameIdentification <OrgnlMsgNmId> [0..1] Text 30
   FileReference <FileRef> [0..1] Text 30
   Recipient <Rcpt> [1..1] ± 30
3.4.2.1  BusinessDate <BizDt>
Presence: [0..1]
Definition: Date of the business day of the requested messages the resend function is used for.
Datatype: "ISODate" on page 66
3.4.2.2  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Independent counter for message sequence, which is available once per party technical
address.
Specifies the identification sequence number for a specific couple sender/receiver.
Datatype: "Max35Text" on page 69
3.4.2.3  SequenceRange <SeqRg>
Presence: [0..1]
Definition: Independent counter for a range of message sequences, which are available once per party
technical address.
Specifies the range of identification sequence numbers for a specific couple sender/receiver.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.006.001.01 ResendRequestV01
Target2-Securities - Administration - Maintenance 2023 -
2024
29 March 2024
```

