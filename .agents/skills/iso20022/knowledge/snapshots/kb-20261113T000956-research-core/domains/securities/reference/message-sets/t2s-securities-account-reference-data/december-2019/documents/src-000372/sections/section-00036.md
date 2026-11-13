---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["5 reda.021.001.01 SecuritiesAccountReportV01", "5.4 Message Building Blocks", "5.4.3 ReportOrError <RptOrErr>", "5.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "5.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "5.4.3.1.2.1 SecuritiesAccount <SctiesAcct>"]
file_pages: [40]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 5.4.3.1.2.1 SecuritiesAccount <SctiesAcct>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 40 to 40.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
SecuritiesAccountOrError <SctiesAcctOrErr> contains one of the following
SecuritiesAccountOrBusinessError3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesAccount <SctiesAcct> [1..1]  40
     OpeningDate <OpngDt> [0..1] Date 41
     ClosingDate <ClsgDt> [0..1] Date 41
     HoldIndicator <HldInd> [0..1] Indicator 41
     NegativePosition <NegPos> [0..1] Indicator 42
     Type <Tp> [0..1]  42
{Or       Code <Cd> [1..1] CodeSet 42
Or}       Proprietary <Prtry> [1..1] ± 43
     AccountOwner <AcctOwnr> [1..1] ± 43
     PartyType <PtyTp> [0..1]  43
{Or       Code <Cd> [1..1] CodeSet 43
Or}       Proprietary <Prtry> [1..1] Text 44
     MarketSpecificAttribute <MktSpcfcAttr> [0..*]  44
       Name <Nm> [1..1] Text 44
       Value <Val> [1..1] Text 44
     Restriction <Rstrctn> [0..*]  44
       ValidFrom <VldFr> [1..1] DateTime 44
       ValidTo <VldTo> [0..1] DateTime 45
       Type <Tp> [1..1] Text 45
     EndInvestorFlag <EndInvstrFlg> [0..1] Text 45
     PricingScheme <PricgSchme> [0..1] Text 45
Or}   BusinessError <BizErr> [1..*]  45
     Error <Err> [1..1]  45
{Or       Code <Cd> [1..1] CodeSet 46
Or}       Proprietary <Prtry> [1..1] Text 46
     Description <Desc> [0..1] Text 46
5.4.3.1.2.1  SecuritiesAccount <SctiesAcct>
Presence: [1..1]
Definition: Specifies the data requested for the securities account.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities - Securities Account Reference Data 40 December 2019
```

