---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "24.3 Constraints"]
file_pages: [786, 787]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
topic_continuations: [{"constraint_ids": ["C21", "C22", "C23", "C24", "C25"], "until_heading": "24.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 788, "topic": "24.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00519.md"}]
---

# 24.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 786 to 787.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 24.3 Constraints topic continues in [Constraints continuation C21–C25 (file p788)](section-00519.md#file-page-788). Read the text before **24.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 786

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     ExpiryDate <XpryDt> [0..1] ± 798
     CutOffDate <CutOffDt> [0..1] ± 799
     Investor <Invstr> [0..1] ± 799
     DeliveringParty1 <DlvrgPty1> [0..1] ± C16,
C19
799
     ReceivingParty1 <RcvgPty1> [0..1] ± C16,
C19
800
     TransactionSubjectToBuyIn <TxSbjtToBuyIn> [0..1] Indicator 801
   SupplementaryData <SplmtryData> [0..*] ± C24 801
24.3 Constraints
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
C4 DescriptionUsageRule
Description must be used alone as the last resort.
C5 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C6 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C7 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C8 ModificationRequestPresenceRule
At least one securities settlement conditions modification request type must be present.
C9 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 786 March 2026
```

## File page 787

```text
C10 OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and
receiver.
C11 PartyRule
Investor, DeliveringParty1 and ReceivingParty1 cannot be requested to be modified using the
SecuritiesSettlementConditionModificationRequest. These fields are made available in the
SecuritiesSettlementConditionModificationRequest to enable the processing of the request vis-
a-vis the transaction requested to be modified.
C12 QuantityRule
If pre-agreed between account servicer and account owner, then Quantity will be used to
instruct the quantity of securities that should be partially processed, for example, partially
authorised.
C13 ReferencePresenceRule
At least one reference must be present.
C14 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C15 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C16 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C17 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C18 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C19 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C20 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 787 March 2026
```

