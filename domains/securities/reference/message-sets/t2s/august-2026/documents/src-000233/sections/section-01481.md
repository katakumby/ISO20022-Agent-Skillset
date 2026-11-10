---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["38 reda.018.001.01 SecuritiesAccountCreationRequestV01", "38.2 Structure"]
file_pages: [2099]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 38.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2099 to 2099.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2099

```text
38.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctCreReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2100
   SecuritiesAccount <SctiesAcct> [1..1]  2100
     AccountOwner <AcctOwnr> [1..1] ± 2101
     Identification <Id> [1..1] Text 2101
     Type <Tp> [1..1]  2102
{Or       Code <Cd> [1..1] CodeSet 2102
Or}       Proprietary <Prtry> [1..1] ± 2102
     OpeningDate <OpngDt> [1..1] Date 2103
     ClosingDate <ClsgDt> [0..1] Date 2103
     HoldIndicator <HldInd> [1..1] Indicator 2103
     NegativePosition <NegPos> [1..1] Indicator 2103
     MarketSpecificAttribute <MktSpcfcAttr> [0..*]  2103
       Name <Nm> [1..1] Text 2104
       Value <Val> [1..1] Text 2104
     Restriction <Rstrctn> [0..*]  2104
       ValidFrom <VldFr> [1..1] DateTime 2104
       ValidTo <VldTo> [0..1] DateTime 2104
       Type <Tp> [1..1] Text 2104
     EndInvestorFlag <EndInvstrFlg> [0..1] Text 2105
     PricingScheme <PricgSchme> [0..1] Text 2105
   SupplementaryData <SplmtryData> [0..*] ± C3 2105
38.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities 2099 August 2026
```

