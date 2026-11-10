---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.6 Identification Information", "5.1.6.3 GenericIdentification36", "5.1.6.3.1 Identification <Id>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.6.3.1 Identification <Id>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 49
   Issuer <Issr> [1..1] Text 49
   SchemeName <SchmeNm> [0..1] Text 49
5.1.6.3.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Max35Text" on page 69
5.1.6.3.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 69
5.1.6.3.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 69
5.1.7 Miscellaneous
5.1.7.1  MessageHeader7
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 49
   CreationDateTime <CreDtTm> [0..1] DateTime 50
   RequestType <ReqTp> [0..1]  50
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 50
Or     Enquiry <Enqry> [1..1] CodeSet 50
Or}     Proprietary <Prtry> [1..1] ± 50
   OriginalBusinessQuery <OrgnlBizQry> [0..1] ± 51
   QueryName <QryNm> [0..1] Text 51
5.1.7.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
49 March 2024
```

