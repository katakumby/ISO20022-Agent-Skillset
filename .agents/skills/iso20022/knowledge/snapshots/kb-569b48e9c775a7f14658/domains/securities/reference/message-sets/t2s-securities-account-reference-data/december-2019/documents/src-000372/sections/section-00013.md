---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["3 reda.019.001.01 SecuritiesAccountQueryV01", "3.2 Structure"]
file_pages: [15]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.019.001.01"]
---

# 3.2 Structure

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 15 to 15.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 15

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctQry> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 16
   SearchCriteria <SchCrit> [1..1]  17
     AccountIdentification <AcctId> [0..1] Text 18
     AccountServicer <AcctSvcr> [0..1] ± 18
     AccountOwner <AcctOwnr> [0..1] ± 19
     PartyType <PtyTp> [0..1]  19
{Or       Code <Cd> [1..1] CodeSet 19
Or}       Proprietary <Prtry> [1..1] Text 19
     OpeningDate <OpngDt> [0..1]  19
{Or       FromDate <FrDt> [1..1] Date 20
Or       ToDate <ToDt> [1..1] Date 20
Or       FromToDate <FrToDt> [1..1] ± 20
Or       EqualDate <EQDt> [1..1] Date 20
Or}       NotEqualDate <NEQDt> [1..1] Date 20
     ClosingDate <ClsgDt> [0..1]  20
{Or       FromDate <FrDt> [1..1] Date 21
Or       ToDate <ToDt> [1..1] Date 21
Or       FromToDate <FrToDt> [1..1] ± 21
Or       EqualDate <EQDt> [1..1] Date 21
Or}       NotEqualDate <NEQDt> [1..1] Date 21
     AccountType <AcctTp> [0..1]  22
{Or       Code <Cd> [1..1] CodeSet 22
Or}       Proprietary <Prtry> [1..1] ± 22
     EndInvestorFlag <EndInvstrFlg> [0..1] Text 23
     PricingScheme <PricgSchme> [0..1] Text 23
   ReturnCriteria <RtrCrit> [0..1]  23
     AccountIdentification <AcctId> [0..1] Indicator 23
     PartyIdentification <PtyId> [0..1] Indicator 23
     PartyType <PtyTp> [0..1] Indicator 24
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.019.001.01 SecuritiesAccountQueryV01
Target2-Securities - Securities Account Reference Data 15 December 2019
```

