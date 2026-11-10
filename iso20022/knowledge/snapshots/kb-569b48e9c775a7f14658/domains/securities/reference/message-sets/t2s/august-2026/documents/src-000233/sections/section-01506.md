---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["41 reda.021.001.01 SecuritiesAccountReportV01", "41.2 Structure"]
file_pages: [2125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.021.001.01"]
---

# 41.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2125 to 2125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2125

```text
41.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctRpt> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2126
   Pagination <Pgntn> [1..1] ± 2127
   ReportOrError <RptOrErr> [1..1]  2127
{Or     SecuritiesAccountReport <SctiesAcctRpt> [1..*]  2129
       SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 2130
       SecuritiesAccountOrError <SctiesAcctOrErr> [1..1]  2131
{Or         SecuritiesAccount <SctiesAcct> [1..1]  2132
           OpeningDate <OpngDt> [0..1] Date 2133
           ClosingDate <ClsgDt> [0..1] Date 2133
           HoldIndicator <HldInd> [0..1] Indicator 2133
           NegativePosition <NegPos> [0..1] Indicator 2134
           Type <Tp> [0..1]  2134
{Or             Code <Cd> [1..1] CodeSet 2134
Or}             Proprietary <Prtry> [1..1] ± 2135
           AccountOwner <AcctOwnr> [1..1] ± 2135
           PartyType <PtyTp> [0..1]  2135
{Or             Code <Cd> [1..1] CodeSet 2135
Or}             Proprietary <Prtry> [1..1] Text 2136
           MarketSpecificAttribute <MktSpcfcAttr> [0..*]  2136
             Name <Nm> [1..1] Text 2136
             Value <Val> [1..1] Text 2136
           Restriction <Rstrctn> [0..*]  2136
             ValidFrom <VldFr> [1..1] DateTime 2136
             ValidTo <VldTo> [0..1] DateTime 2137
             Type <Tp> [1..1] Text 2137
           EndInvestorFlag <EndInvstrFlg> [0..1] Text 2137
           PricingScheme <PricgSchme> [0..1] Text 2137
Or}         BusinessError <BizErr> [1..*]  2137
           Error <Err> [1..1]  2137
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.021.001.01 SecuritiesAccountReportV01
Target2-Securities 2125 August 2026
```

