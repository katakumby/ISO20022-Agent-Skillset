---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.14 CorporateActionEventType56Choice", "82.1.19.14.2 Proprietary <Prtry>"]
file_pages: [2993]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.14.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2993 to 2993.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2993

```text
CodeName Name Definition
been distributed to investors for tax
purposes.
MTNG SecuritiesHoldersMeeting Ordinary or annual or extraordinary or
special general meeting.
INFO Information Information provided by the issuer
having no accounting/financial impact on
the holder.
82.1.19.14.2  Proprietary <Prtry>
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
82.1.19.15  Tracking4Choice
Definition: Choice of format for the tracking information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 2993
Or}   Proprietary <Prtry> [1..1] ± 2993
82.1.19.15.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the loan and/or collateral is tracked.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.19.15.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Tracking information expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2993 August 2026
```

