---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.3 Constraints"]
file_pages: [324, 325, 326, 327, 328, 329]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.3 Constraints

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 324 to 329.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 324

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     SafekeepingAccount <SfkpgAcct> [0..1] Text 351
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 351
     CashAccount <CshAcct> [0..1] ± 351
     SafekeepingPlace <SfkpgPlc> [0..1] ± 352
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C13,
C14,
C19,
C20,
C23
352
     TotalEligibleBalance <TtlElgblBal> [0..1] ± 353
     InstructedBalance <InstdBal> [0..1] ± 354
     UninstructedBalance <UinstdBal> [0..1] ± 354
     ProtectBalance <PrtctBal> [0..1] ± 355
     StatusQuantity <StsQty> [0..1] ± 355
     StatusCashAmount <StsCshAmt> [0..1] Amount C1, C12 356
     SolicitationDealerFeeIndicator <SlctnDealrFeeInd> [0..1] Indicator 356
   ProtectInstruction <PrtctInstr> [0..1]  356
     TransactionType <TxTp> [1..1] CodeSet 357
     ProtectTransactionStatus <PrtctTxSts> [0..1] CodeSet 357
     TransactionIdentification <TxId> [0..1] Text 357
     ProtectSafekeepingAccount <PrtctSfkpgAcct> [0..1] Text 358
     ProtectDate <PrtctDt> [0..1] Date 358
     UncoveredProtectQuantity <UcvrdPrtctQty> [0..1] ± 358
   AdditionalInformation <AddtlInf> [0..1]  358
     AdditionalText <AddtlTxt> [0..*] Text 358
     PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 358
   SupplementaryData <SplmtryData> [0..*] ± C38 359
6.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 324 February 2026
```

## File page 325

```text
C2 AdditionalInformationRule
All elements in the AdditionalInformation element must not contain information that can be
provided in a structured field unless bilaterally agreed.
This constraint is defined at the MessageDefinition level.
C3 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C5 AdditionalReasonInforrmationRule
AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
C6 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C7 AdditionalReasonInforrmationRule
AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
C8 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C9 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C10 BeneficialOwnerBreakdownRequestRule
If CorporateActionInstruction/OptionType/Code value is BOBD
(BeneficialOwnerBreakdownRequest), then CorporateActionGeneralInformation/EventType/
Code value must be WTRC (Withholding Tax Relief Certification).
(MT567 NVR C6)
On Condition
    /CorporateActionInstruction/OptionType/Code is equal to value 
'BeneficialOwnerBreakdownRequest'
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'WithholdingTaxReliefCertification'
This constraint is defined at the MessageDefinition level.
C11 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 325 February 2026
```

## File page 326

```text
C12 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C13 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C14 DescriptionUsageRule
Description must be used alone as the last resort.
C15 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C16 EventTypeRule
EventType/Code OTHR must only be used in case no other corporate action event code is
appropriate.
EventType/Code CHAN must only be used in case no other corporate action event code is
appropriate and only for an event which relates to a change.
EventType/Code REDM must only be used when the redemption is decided by the issuer and
not by the securities holders.
C17 EventTypeRule
If Code is present, the code OTHR must only be used in case no other corporate action event
code is appropriate.
If Code is present, the code CHAN must only be used in case no other corporate action event
code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM must only be used when the redemption is decided by the
issuer and not by the securities holders.
C18 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C19 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C20 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C21 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 326 February 2026
```

## File page 327

```text
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C22 OptionNumberRule
For differentiation between options, the OptionNumber rather than the OptionType must be
used, for example, in the case where two or more offers can be described by the same
corporate action option code. Therefore, the OptionNumber value must be different for each
option.
C23 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C24 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C25 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C26 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C27 SafekeepingPlaceRule
SafekeepingPlace must only be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C28 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C29 StatusQuantity1Rule
If CorporateActionInstruction/StatusCashAmount is present, then the
InstructionProcessingStatus/Cancelled/CancelledQuantity and InstructionProcessingStatus/
AcceptedForFurtherProcessing/AcceptedQuantity and InstructionProcessingStatus/Rejected
and InstructionProcessingStatus/Pending must be absent and CorporateActionInstruction/
StatusQuantity must be absent. (MT 567 C5 and C7).
On Condition
    /CorporateActionInstruction/StatusCashAmount is present
Following Must be True
    /InstructionProcessingStatus[*]/Cancelled/CancelledQuantity Must be absent
 And    /InstructionProcessingStatus[*]/AcceptedForFurtherProcessing/
AcceptedQuantity Must be absent
 And    /InstructionProcessingStatus[*]/Rejected Must be absent
 And    /InstructionProcessingStatus[*]/Pending Must be absent
 And    /CorporateActionInstruction/StatusQuantity Must be absent
This constraint is defined at the MessageDefinition level.
C30 StatusQuantity1UGRule
If CorporateActionInstruction/StatusCashAmount is present, then the
InstructionProcessingStatus/Cancelled/CancelledQuantity and InstructionProcessingStatus/
AcceptedForFurtherProcessing/AcceptedQuantity and InstructionProcessingStatus/Rejected
and InstructionProcessingStatus/Pending must be absent and CorporateActionInstruction/
StatusQuantity must be absent. (MT 567 C5 and C7).
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 327 February 2026
```

## File page 328

```text
if 
    at least one occurrence of the following element(s) 
[CorporateActionInstruction/StatusCashAmount] is (are) present 
, then 
    the following element(s) [InstructionProcessingStatus/Cancelled/
CancelledQuantity] and [InstructionProcessingStatus/
AcceptedForFurtherProcessing/AcceptedQuantity] and 
[InstructionProcessingStatus/Forwarded/ForwardedQuantity] and 
[InstructionProcessingStatus/Rejected/RejectedQuantity] and 
[InstructionProcessingStatus/Pending/PendingQuantity] and 
[InstructionProcessingStatus/Returned/ReturnedQuantity] and 
[InstructionProcessingStatus/ReceivedByIssuerOrOfferor/
AcceptedByIssuerQuantity] and [CorporateActionInstruction/StatusQuantity] 
must be absent 
Expression Language: UGRule
This constraint is defined at the MessageDefinition level.
C31 StatusQuantity2Rule
If CorporateActionInstruction/StatusQuantity is present, then the InstructionProcessingStatus/
Cancelled/CancelledQuantity and InstructionProcessingStatus/AcceptedForFurtherProcessing/
AcceptedQuantity and InstructionProcessingStatus/Rejected and InstructionProcessingStatus/
Pending must be absent and CorporateActionInstruction/StatusCashAmount must be absent.
(MT 567 C5 and C7).
On Condition
    /CorporateActionInstruction/StatusQuantity is present
Following Must be True
    /InstructionProcessingStatus[*]/Cancelled/CancelledQuantity Must be absent
 And    /InstructionProcessingStatus[*]/AcceptedForFurtherProcessing/
AcceptedQuantity Must be absent
 And    /InstructionProcessingStatus[*]/Rejected Must be absent
 And    /InstructionProcessingStatus[*]/Pending Must be absent
 And    /CorporateActionInstruction/StatusCashAmount Must be absent
This constraint is defined at the MessageDefinition level.
C32 StatusQuantity2UGRule
If CorporateActionInstruction/StatusQuantity is present, then the InstructionProcessingStatus/
Cancelled/CancelledQuantity and InstructionProcessingStatus/AcceptedForFurtherProcessing/
AcceptedQuantity and InstructionProcessingStatus/Rejected and InstructionProcessingStatus/
Pending must be absent and CorporateActionInstruction/StatusCashAmount must be absent.
(MT 567 C5 and C7)
if 
    at least one occurrence of the following element(s) 
[CorporateActionInstruction/StatusQuantity] is (are) present 
, then 
    the following element(s) [InstructionProcessingStatus/Cancelled/
CancelledQuantity] and [InstructionProcessingStatus/
AcceptedForFurtherProcessing/AcceptedQuantity] and 
[InstructionProcessingStatus/Forwarded/ForwardedQuantity] and 
[InstructionProcessingStatus/Rejected/RejectedQuantity] and 
[InstructionProcessingStatus/Pending/PendingQuantity] and 
[InstructionProcessingStatus/Returned/ReturnedQuantity] and 
[InstructionProcessingStatus/ReceivedByIssuerOrOfferor/
AcceptedByIssuerQuantity] and [CorporateActionInstruction/StatusCashAmount] 
must be absent 
Expression Language: UGRule
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 328 February 2026
```

## File page 329

```text
C33 StatusQuantity3Rule
If InstructionProcessingStatus/Cancelled/CancelledQuantity or InstructionProcessingStatus/
AcceptedForFurtherProcessing/AcceptedQuantity or InstructionProcessingStatus/Rejected or
InstructionProcessingStatus/Pending are present, then CorporateActionInstruction/
StatusCashAmount and CorporateActionInstruction/StatusQuantity must be absent. (MT 567
C5 and C7).
On Condition
    /InstructionProcessingStatus[*]/Cancelled/CancelledQuantity is present
 Or    /InstructionProcessingStatus[*]/AcceptedForFurtherProcessing/
AcceptedQuantity is present
 Or    /InstructionProcessingStatus[*]/Rejected/RejectedQuantity is present
 Or    /InstructionProcessingStatus[*]/Pending/PendingQuantity is present
Following Must be True
    /CorporateActionInstruction/StatusQuantity Must be absent
 And    /CorporateActionInstruction/StatusCashAmount Must be absent
This constraint is defined at the MessageDefinition level.
C34 StatusQuantity3UGRule
If InstructionProcessingStatus/Cancelled/CancelledQuantity or InstructionProcessingStatus/
AcceptedForFurtherProcessing/AcceptedQuantity or InstructionProcessingStatus/Rejected or
InstructionProcessingStatus/Pending are present, then CorporateActionInstruction/
StatusCashAmount and CorporateActionInstruction/StatusQuantity must be absent. (MT 567
C5 and C7).
if 
    at least one occurrence of the following element(s) 
[InstructionProcessingStatus/Cancelled/CancelledQuantity] and 
[InstructionProcessingStatus/AcceptedForFurtherProcessing/AcceptedQuantity] 
and [InstructionProcessingStatus/Forwarded/ForwardedQuantity] and 
[InstructionProcessingStatus/Rejected/RejectedQuantity] and 
[InstructionProcessingStatus/Pending/PendingQuantity] and 
[InstructionProcessingStatus/Returned/ReturnedQuantity] and 
[InstructionProcessingStatus/ReceivedByIssuerOrOfferor/
AcceptedByIssuerQuantity] is (are) present 
, then 
    the following element(s) [CorporateActionInstruction/StatusQuantity] and 
[CorporateActionInstruction/StatusCashAmount] must be absent 
Expression Language: UGRule
This constraint is defined at the MessageDefinition level.
C35 StatusQuantity4Rule
If CorporateActionInstruction/StatusCashAmount is present, then the
InstructionProcessingStatus/Forwarded/ForwardedQuantity and InstructionProcessingStatus/
Returned/ReturnedQuantity and InstructionProcessingStatus/ReceivedByIssuerOrOfferor/
AcceptedByIssuerQuantity Must be absent.
On Condition
    /CorporateActionInstruction/StatusCashAmount is present
Following Must be True
    /InstructionProcessingStatus[*]/Forwarded/ForwardedQuantity Must be absent
 And    /InstructionProcessingStatus[*]/Returned/ReturnedQuantity Must be 
absent
 And    /InstructionProcessingStatus[*]/ReceivedByIssuerOrOfferor/
AcceptedByIssuerQuantity Must be absent
 And    /CorporateActionInstruction/StatusQuantity Must be absent
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 329 February 2026
```

