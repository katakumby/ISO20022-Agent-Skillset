---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "4.2 Structure"]
file_pages: [137, 138, 139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.013.001.07"]
---

# 4.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 137 to 139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 137

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraPosMvmntInstr> [1..1]  C17,
C18,
C19
   TransactionIdentification <TxId> [1..1] Text 140
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 140
   NumberCounts <NbCounts> [0..1] ± C8 140
   Linkages <Lnkgs> [0..*] ± 140
   AccountOwner <AcctOwnr> [0..1] ± 141
   SafekeepingAccount <SfkpgAcct> [0..1] ± 141
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 141
   SafekeepingPlace <SfkpgPlc> [0..1] ± 142
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C10,
C11,
C13,
C14,
C15
142
   FinancialInstrumentAttributes <FinInstrmAttrbts> [0..1] ± C2, C16 143
   IntraPositionDetails <IntraPosDtls> [1..1]  C3, C5 146
     Priority <Prty> [0..1] ± 147
     SettlementQuantity <SttlmQty> [1..1] ± C12 147
     SecuritiesSubBalanceIdentification <SctiesSubBalId> [0..1] ± 148
     SettlementDate <SttlmDt> [1..1] ± 148
     BalanceFrom <BalFr> [1..1] ± 148
     BalanceTo <BalTo> [1..1] ± 149
     InstructionProcessingAdditionalDetails <InstrPrcgAddtlDtls> [0..1] Text 149
   SupplementaryData <SplmtryData> [0..*] ± C21 149
4.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 137 March 2026
```

## File page 138

```text
C2 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
FinancialInstrumentAttributeAdditionalDetails is present, then it must not contain information
that can be provided in a structured field.
C3 AdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if
InstructionProcessingAdditionalDetails is present, then it must not contain information that can
be provided in a structured field.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 BalanceFromToRule
The SecuritiesBalanceType of BalanceFrom must be different from the SecuritiesBalanceType
of BalanceTo.
C6 BlockTradeGuideline
In a block trade instruction, the total number of children must be provided using
TotalOfLinkedInstructions.
The CurrentInstructionNumber of the parent must be 000. The children must have an
incremental CurrentInstructionNumber from 001 to 999.
For more details, see the relevant market practice document on www.smpg.info.
C7 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C8 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
C9 CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement
instruction, then the CurrentInstructionNumber must be specified.
C10 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C11 DescriptionUsageRule
Description must be used alone as the last resort.
C12 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 138 March 2026
```

## File page 139

```text
C13 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C14 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C15 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C16 PlaceOfListingRule
If PlaceOfListing is used and an ISO 10383 MIC exists for the market to be identified, the ISO
10383 Market Identifier Code (MIC) must be used.
C17 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C18 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C19 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C20 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C21 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C22 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 139 March 2026
```

