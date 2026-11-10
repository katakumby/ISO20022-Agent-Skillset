---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.17 EUCapitalGainType3Choice"]
file_pages: [307]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.17 EUCapitalGainType3Choice

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 307 to 307.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 307

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.17  EUCapitalGainType3Choice
Definition: Choice of an EU capital gain type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   EUCapitalGain <EUCptlGn> [1..1] CodeSet 307
Or}   Proprietary <Prtry> [1..1] ± 307
7.1.19.17.1  EUCapitalGain <EUCptlGn>
Presence: [1..1]
Definition: Specifies whether capital gain is in the scope of the European directive on taxation of
savings income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income
realised upon sale, a refund or redemption of shares and units, etc.
Datatype: "EUCapitalGain2Code" on page 624
CodeName Name Definition
EUSI CapitalGainInScope Capital gain is in the scope of the
directive.
EUSO CapitalGainOutScope Capital gain is out of the scope of the
directive.
UKWN CapitalGainUnknown Unknown whether capital gain is in or
out of the scope of the directive.
7.1.19.17.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies whether capital gain is in the scope of the European directive on taxation of
savings income in the form of interest payments (Council Directive 2003/48/EC 3 June), or an income
realised upon sale, a refund or redemption of shares and units, etc.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 307 February 2025
```

