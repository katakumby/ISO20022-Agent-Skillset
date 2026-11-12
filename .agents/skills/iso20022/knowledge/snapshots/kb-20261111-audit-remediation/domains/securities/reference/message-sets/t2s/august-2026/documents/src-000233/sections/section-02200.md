---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.17 Identification Information", "82.1.17.1 TransactionIdentifications55", "82.1.17.1.10 CorporateActionEventIdentification <CorpActnEvtId>"]
file_pages: [2963]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.17.1.10 CorporateActionEventIdentification <CorpActnEvtId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2963 to 2963.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2963

```text
Definition: Identification assigned by the netting service provider to identify the net transaction resulting
from the netting process.
Datatype: "Max35Text" on page 3328
82.1.17.1.10  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 3328
82.1.17.1.11  RelatedTransactionIdentification <RltdTxId>
Presence: [0..1]
Definition: Matching reference
Datatype: "Max35Text" on page 3328
82.1.17.2  GenericIdentification80
Definition: Identification expressed as a proprietary type and narrative description.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 2963
   Identification <Id> [0..1] Text 2963
82.1.17.2.1  Type <Tp>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.17.2.2  Identification <Id>
Presence: [0..1]
Definition: Name or number assigned by an entity to enable recognition of that entity.
Datatype: "Max35Text" on page 3328
82.1.17.3  IdentificationType42Choice
Definition: Choice between a code and a data source scheme to specify the type of alternate
identification.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2963 August 2026
```

