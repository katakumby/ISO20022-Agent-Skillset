---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["10 seev.038.001.09 CorporateActionNarrativeV09", "10.2 Structure"]
file_pages: [693]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.038.001.09"]
---

# 10.2 Structure

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 693 to 693.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 693

```text
10.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CorpActnNrrtv> [1..1]  
   AccountDetails <AcctDtls> [0..1]  694
{Or     ForAllAccounts <ForAllAccts> [1..1] ± 695
Or}     AccountsListAndBalanceDetails <AcctsListAndBalDtls> [1..*]  C10,
C11,
C12,
C13
695
       SafekeepingAccount <SfkpgAcct> [0..1] Text 696
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 696
       AccountOwner <AcctOwnr> [0..1] ± 696
       SafekeepingPlace <SfkpgPlc> [0..1] ± 697
       ConfirmedBalance <ConfdBal> [1..1] ± 697
   UnderlyingSecurity <UndrlygScty> [0..1] ± C3, C4,
C6, C7,
C9
697
   CorporateActionGeneralInformation <CorpActnGnlInf> [1..1]  C8 698
     CorporateActionEventIdentification <CorpActnEvtId> [1..1] Text 699
     OfficialCorporateActionEventIdentification
<OffclCorpActnEvtId>
[0..1] Text 699
     NarrativeType <NrrtvTp> [0..1] ± 699
   AdditionalInformation <AddtlInf> [1..*] Text 700
   SupplementaryData <SplmtryData> [0..*] ± C14 700
10.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
Approved by the Securities SEG on 27 January 2026 seev.038.001.09 CorporateActionNarrativeV09
Corporate Actions - Maintenance 2025 - 2026 693 February 2026
```

