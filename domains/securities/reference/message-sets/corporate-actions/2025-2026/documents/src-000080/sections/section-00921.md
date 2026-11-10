---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.25 Settlement Chain", "16.1.25.1 SettlementParties129", "16.1.25.1.4 Party3 <Pty3>"]
file_pages: [1139]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.25.1.4 Party3 <Pty3>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1139 to 1139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1139

```text
Following Must be True
    /BlockChainAddressOrWallet Must be absent
16.1.25.1.4  Party3 <Pty3>
Presence: [0..1]
Definition: Party that interacts with the party2.
Impacted by: C4 "AdditionalInforrmationRule", C54 "SafekeepingAccountOrBlockChainAddress1Rule",
C56 "SafekeepingAccountOrBlockChainAddress2Rule", C58
"SafekeepingAccountOrBlockChainAddress3Rule"
Party3 <Pty3> contains the following elements (see "PartyIdentificationAndAccount204" on page 1038
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1039
   SafekeepingAccount <SfkpgAcct> [0..1] Text 1039
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 1039
   ProcessingIdentification <PrcgId> [0..1] Text 1040
   AlternateIdentification <AltrnId> [0..*] ± 1040
Constraints
• AdditionalInforrmationRule
The AdditionalInformation field in all elements must not contain information that can be provided in a
structured field unless bilaterally agreed or advised differently in the element definition as in
NarrativeVersion.
• SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
• SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1139 February 2026
```

