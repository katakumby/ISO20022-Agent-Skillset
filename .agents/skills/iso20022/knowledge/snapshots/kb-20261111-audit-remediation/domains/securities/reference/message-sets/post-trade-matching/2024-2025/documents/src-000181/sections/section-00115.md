---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["5 setr.030.001.03 SecuritiesTradeConfirmationResponseV03", "5.2 Structure"]
file_pages: [149]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.030.001.03"]
---

# 5.2 Structure

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 149 to 149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 149

```text
F. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTradConfRspn> [1..1]  
   Identification <Id> [1..1]  150
     TransactionIdentification <TxId> [1..1] Text 151
   References <Refs> [1..*] ± 151
   Status <Sts> [1..1]  C1, C10 151
     AffirmationStatus <AffirmSts> [1..1] ± 151
     UnaffirmedReason <UaffrmdRsn> [0..1] ± 152
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 152
   ClearingDetails <ClrDtls> [0..1]  152
     ClearingMember <ClrMmb> [1..*] ± 152
     ClearingSegment <ClrSgmt> [0..1] ± 153
   ConfirmationParties <ConfPties> [0..*]  154
     AffirmingParty <AffrmgPty> [1..1] ± 154
     Buyer <Buyr> [0..1] ± 155
     Borrower <Brrwr> [0..1] ± 156
     Seller <Sellr> [0..1] ± 157
     Lender <Lndr> [0..1] ± 158
     TradeBeneficiaryParty <TradBnfcryPty> [0..1] ± 159
   SupplementaryData <SplmtryData> [0..*] ± C9 160
5.3 Constraints
C1 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C2 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
Approved by the Securities SEG on 13 February 2025 setr.030.001.03
SecuritiesTradeConfirmationResponseV03
Post Trade Matching - Maintenance 2024 - 2025 149 February 2025
```

