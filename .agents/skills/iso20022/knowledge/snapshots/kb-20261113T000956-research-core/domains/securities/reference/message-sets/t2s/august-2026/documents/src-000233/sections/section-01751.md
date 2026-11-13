---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["70 semt.025.001.01 SecuritiesAccountPositionQueryV01", "70.2 Structure"]
file_pages: [2402]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 70.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2402 to 2402.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2402

```text
70.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctPosQry> [1..1]  
   Statement <Stmt> [1..1] ± 2403
   SearchCriteria <SchCrit> [1..1]  2403
     AccountOwner <AcctOwnr> [0..1] ± 2404
     AccountServicer <AcctSvcr> [0..1] ± 2404
     SafekeepingAccount <SfkpgAcct> [0..1] ± 2404
     FinancialInstrument <FinInstrm> [0..1] ± C4, C5,
C7, C8,
C9
2405
     CountryOfIssue <CtryOfIsse> [0..1] CodeSet C3 2406
     SubBalanceType <SubBalTp> [0..1] ± 2406
     ReturnZeroPosition <RtrZeroPos> [1..1] Indicator 2406
     OtherBusinessParties <OthrBizPties> [0..1]  2407
       Investor <Invstr> [0..*] ± C6, C10,
C11
2407
   SupplementaryData <SplmtryData> [0..*] ± C12 2408
70.3 Constraints
C1 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C5 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities 2402 August 2026
```

