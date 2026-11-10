---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["2 reda.018.001.01 SecuritiesAccountCreationRequestV01", "2.2 Structure"]
file_pages: [7]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 2.2 Structure

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 7 to 7.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 7

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 8
   SecuritiesAccount <SctiesAcct> [1..1]  8
     AccountOwner <AcctOwnr> [1..1] ± 9
     Identification <Id> [1..1] Text 9
     Type <Tp> [1..1]  10
{Or       Code <Cd> [1..1] CodeSet 10
Or}       Proprietary <Prtry> [1..1] ± 10
     OpeningDate <OpngDt> [1..1] Date 11
     ClosingDate <ClsgDt> [0..1] Date 11
     HoldIndicator <HldInd> [1..1] Indicator 11
     NegativePosition <NegPos> [1..1] Indicator 11
     MarketSpecificAttribute <MktSpcfcAttr> [0..*]  11
       Name <Nm> [1..1] Text 12
       Value <Val> [1..1] Text 12
     Restriction <Rstrctn> [0..*]  12
       ValidFrom <VldFr> [1..1] DateTime 12
       ValidTo <VldTo> [0..1] DateTime 12
       Type <Tp> [1..1] Text 12
     EndInvestorFlag <EndInvstrFlg> [0..1] Text 13
     PricingScheme <PricgSchme> [0..1] Text 13
   SupplementaryData <SplmtryData> [0..*] ± C3 13
2.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities - Securities Account Reference Data 7 December 2019
```

