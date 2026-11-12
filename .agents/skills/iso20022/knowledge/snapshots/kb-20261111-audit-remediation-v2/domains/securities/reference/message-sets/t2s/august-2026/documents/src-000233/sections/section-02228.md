---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.17 MessageHeader3", "82.1.19.17.5 QueryName <QryNm>"]
file_pages: [2997]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.17.5 QueryName <QryNm>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2997 to 2997.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2997

```text
OriginalBusinessQuery <OrgnlBizQry> contains the following elements (see
"OriginalBusinessQuery1" on page 3043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3043
   MessageNameIdentification <MsgNmId> [0..1] Text 3043
   CreationDateTime <CreDtTm> [0..1] DateTime 3043
82.1.19.17.5  QueryName <QryNm>
Presence: [0..1]
Definition: Recalls the criteria (search and return criteria) defined in a preceding query.
Datatype: "Max35Text" on page 3328
82.1.19.18  SecuritiesRTGS4Choice
Definition: Choice of format for the securities RTGS information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 2997
Or}   Proprietary <Prtry> [1..1] ± 2997
82.1.19.18.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.19.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities RTGS information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2997 August 2026
```

