---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["41 reda.021.001.01 SecuritiesAccountReportV01", "41.4 Message Building Blocks", "41.4.3 ReportOrError <RptOrErr>", "41.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "41.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "41.4.3.1.2.1 SecuritiesAccount <SctiesAcct>", "41.4.3.1.2.1.9 Restriction <Rstrctn>", "41.4.3.1.2.1.9.2 ValidTo <VldTo>"]
file_pages: [2137]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 41.4.3.1.2.1.9.2 ValidTo <VldTo>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2137 to 2137.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2137

```text
41.4.3.1.2.1.9.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Specifies the date until which the restriction is valid.
Datatype: "ISODateTime" on page 3320
41.4.3.1.2.1.9.3  Type <Tp>
Presence: [1..1]
Definition: Specifies the identification of a restriction.
Datatype: "Max35Text" on page 3328
41.4.3.1.2.1.10  EndInvestorFlag <EndInvstrFlg>
Presence: [0..1]
Definition: Specifies information to identify securities accounts where allocation instructions are posted.
Datatype: "Exact4AlphaNumericText" on page 3325
41.4.3.1.2.1.11  PricingScheme <PricgSchme>
Presence: [0..1]
Definition: Defines how the price is applied to the securities account.
Datatype: "Exact4AlphaNumericText" on page 3325
41.4.3.1.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Business error resulting from a rejection.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  2137
{Or     Code <Cd> [1..1] CodeSet 2138
Or}     Proprietary <Prtry> [1..1] Text 2138
   Description <Desc> [0..1] Text 2138
41.4.3.1.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2138
Or}   Proprietary <Prtry> [1..1] Text 2138
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities 2137 August 2026
```

