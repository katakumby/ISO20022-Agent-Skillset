---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.32 SettlementOrCorporateActionEvent27Choice"]
file_pages: [3015]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.32 SettlementOrCorporateActionEvent27Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3015 to 3015.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3015

```text
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.32  SettlementOrCorporateActionEvent27Choice
Definition: Choice between transaction type, corporate action event and settlement transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 3015
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 3015
82.1.19.32.1  SecuritiesTransactionType <SctiesTxTp>
Presence: [1..1]
Definition: Identifies the type of securities transaction.
SecuritiesTransactionType <SctiesTxTp> contains one of the following elements (see
"SecuritiesTransactionType44Choice" on page 3036 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3036
Or}   Proprietary <Prtry> [1..1] ± 3039
82.1.19.32.2  CorporateActionEventType <CorpActnEvtTp>
Presence: [1..1]
Definition: Specifies the type of corporate event.
Impacted by: C13 "EventTypeRule"
CorporateActionEventType <CorpActnEvtTp> contains one of the following elements (see
"CorporateActionEventType73Choice" on page 3049 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3049
Or}   Proprietary <Prtry> [1..1] ± 3056
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3015 August 2026
```

