---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.64 CorporateActionEventType73Choice", "82.1.19.64.2 Proprietary <Prtry>"]
file_pages: [3056]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.64.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3056 to 3056.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3056

```text
CodeName Name Definition
been distributed to investors for tax
purposes.
MTNG SecuritiesHoldersMeeting Ordinary or annual or extraordinary or
special general meeting.
INFO Information Information provided by the issuer
having no accounting/financial impact on
the holder.
TNDP TaxOnNonDistributedProceeds Taxable component on non-distributed
proceeds, for example, Australian
deemed income or US 871m income
regulation.
82.1.19.64.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Corporate action event type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.65  LinkageType3Choice
Definition: Choice of format for the linkage type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3056
Or}   Proprietary <Prtry> [1..1] ± 3057
82.1.19.65.1  Code <Cd>
Presence: [1..1]
Definition: Linkage type expressed as an ISO 20022 code.
Datatype: "LinkageType1Code" on page 3262
CodeName Name Definition
LINK Link Request is to link the referenced
transactions.
UNLK Unlink Request is to unlink the referenced
transactions.
SOFT Soft Request is to soft link the referenced
transactions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3056 August 2026
```

