---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["5 reda.021.001.01 SecuritiesAccountReportV01", "5.4 Message Building Blocks", "5.4.3 ReportOrError <RptOrErr>", "5.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "5.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "5.4.3.1.2.1 SecuritiesAccount <SctiesAcct>", "5.4.3.1.2.1.9 Restriction <Rstrctn>", "5.4.3.1.2.1.9.2 ValidTo <VldTo>"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 5.4.3.1.2.1.9.2 ValidTo <VldTo>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
5.4.3.1.2.1.9.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Specifies the date until which the restriction is valid.
Datatype: "ISODateTime" on page 97
5.4.3.1.2.1.9.3  Type <Tp>
Presence: [1..1]
Definition: Specifies the identification of a restriction.
Datatype: "Max35Text" on page 100
5.4.3.1.2.1.10  EndInvestorFlag <EndInvstrFlg>
Presence: [0..1]
Definition: Specifies information to identify securities accounts where allocation instructions are posted.
Datatype: "Exact4AlphaNumericText" on page 99
5.4.3.1.2.1.11  PricingScheme <PricgSchme>
Presence: [0..1]
Definition: Defines how the price is applied to the securities account.
Datatype: "Exact4AlphaNumericText" on page 99
5.4.3.1.2.2  BusinessError <BizErr>
Presence: [1..*]
Definition: Business error resulting from a rejection.
BusinessError <BizErr> contains the following ErrorHandling5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  45
{Or     Code <Cd> [1..1] CodeSet 46
Or}     Proprietary <Prtry> [1..1] Text 46
   Description <Desc> [0..1] Text 46
5.4.3.1.2.2.1  Error <Err>
Presence: [1..1]
Definition: Specification of the error, in coded or proprietary form.
Error <Err> contains one of the following ErrorHandling3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 46
Or}   Proprietary <Prtry> [1..1] Text 46
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities - Securities Account Reference Data 45 December 2019
```

