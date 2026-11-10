---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["41 reda.021.001.01 SecuritiesAccountReportV01", "41.4 Message Building Blocks", "41.4.3 ReportOrError <RptOrErr>", "41.4.3.1 SecuritiesAccountReport <SctiesAcctRpt>", "41.4.3.1.2 SecuritiesAccountOrError <SctiesAcctOrErr>", "41.4.3.1.2.1 SecuritiesAccount <SctiesAcct>"]
file_pages: [2132]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 41.4.3.1.2.1 SecuritiesAccount <SctiesAcct>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2132 to 2132.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2132

```text
SecuritiesAccountOrError <SctiesAcctOrErr> contains one of the following
SecuritiesAccountOrBusinessError3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesAccount <SctiesAcct> [1..1]  2132
     OpeningDate <OpngDt> [0..1] Date 2133
     ClosingDate <ClsgDt> [0..1] Date 2133
     HoldIndicator <HldInd> [0..1] Indicator 2133
     NegativePosition <NegPos> [0..1] Indicator 2134
     Type <Tp> [0..1]  2134
{Or       Code <Cd> [1..1] CodeSet 2134
Or}       Proprietary <Prtry> [1..1] ± 2135
     AccountOwner <AcctOwnr> [1..1] ± 2135
     PartyType <PtyTp> [0..1]  2135
{Or       Code <Cd> [1..1] CodeSet 2135
Or}       Proprietary <Prtry> [1..1] Text 2136
     MarketSpecificAttribute <MktSpcfcAttr> [0..*]  2136
       Name <Nm> [1..1] Text 2136
       Value <Val> [1..1] Text 2136
     Restriction <Rstrctn> [0..*]  2136
       ValidFrom <VldFr> [1..1] DateTime 2136
       ValidTo <VldTo> [0..1] DateTime 2137
       Type <Tp> [1..1] Text 2137
     EndInvestorFlag <EndInvstrFlg> [0..1] Text 2137
     PricingScheme <PricgSchme> [0..1] Text 2137
Or}   BusinessError <BizErr> [1..*]  2137
     Error <Err> [1..1]  2137
{Or       Code <Cd> [1..1] CodeSet 2138
Or}       Proprietary <Prtry> [1..1] Text 2138
     Description <Desc> [0..1] Text 2138
41.4.3.1.2.1  SecuritiesAccount <SctiesAcct>
Presence: [1..1]
Definition: Specifies the data requested for the securities account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities 2132 August 2026
```

