---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.28 BlockChainAddressWallet3", "16.1.15.28.2 Type <Tp>"]
file_pages: [926]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.28.2 Type <Tp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 926 to 926.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 926

```text
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max140Text" on page 1249
16.1.15.28.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 879 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.28.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 1251
16.1.15.29  NetDividendRateFormat38Choice
Definition: Choice between an amount or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 927
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  927
     Amount <Amt> [1..1] Amount C1 927
     RateStatus <RateSts> [1..1] CodeSet 927
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  928
     RateType <RateTp> [1..1]  928
{Or       Code <Cd> [1..1] CodeSet 928
Or}       Proprietary <Prtry> [1..1] ± 929
     Amount <Amt> [1..1] Amount C1 929
     RateStatus <RateSts> [0..1]  C52 930
{Or       Code <Cd> [1..1] CodeSet 930
Or}       Proprietary <Prtry> [1..1] ± 930
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 930
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 926 February 2026
```

