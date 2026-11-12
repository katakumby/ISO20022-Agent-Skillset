---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.23 Price", "82.1.23.4 TypeOfPrice29Choice", "82.1.23.4.2 Proprietary <Prtry>"]
file_pages: [3104]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.23.4.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3104 to 3104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3104

```text
CodeName Name Definition
AVER Average Price is an average execution price.
82.1.23.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of price expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.23.5  PriceInformation20
Definition: Amount of money for which goods or services are offered, sold, or bought.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3104
   Value <Val> [1..1] ± 3105
   ValueType <ValTp> [1..1] ± 3105
   SourceOfPrice <SrcOfPric> [0..1] ± 3105
   QuotationDate <QtnDt> [0..1] ± 3105
Constraints
• ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
82.1.23.5.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of price and information about the price.
Type <Tp> contains one of the following elements (see "TypeOfPrice28Choice" on page 3107 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3108
Or}   Proprietary <Prtry> [1..1] ± 3109
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3104 August 2026
```

