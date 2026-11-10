---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.3 Constraints"]
file_pages: [736, 737, 738]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 736 to 738.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 736

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 749
     CashAccount <CshAcct> [0..1] ± 749
     SafekeepingPlace <SfkpgPlc> [0..1] ± 750
     FinancialInstrumentIdentification <FinInstrmId> [0..1] ± C11,
C12,
C17,
C18,
C21
750
     TotalEligibleBalance <TtlElgblBal> [0..1] ± 751
     InstructedBalance <InstdBal> [0..1] ± 752
     UninstructedBalance <UinstdBal> [0..1] ± 752
     ProtectBalance <PrtctBal> [0..1] ± 752
     StatusQuantity <StsQty> [0..1] ± 753
     StatusCashAmount <StsCshAmt> [0..1] Amount C1, C10 753
   ProtectInstruction <PrtctInstr> [0..1]  754
     TransactionType <TxTp> [1..1] CodeSet 754
     ProtectTransactionStatus <PrtctTxSts> [0..1] CodeSet 754
     TransactionIdentification <TxId> [0..1] Text 754
     ProtectDate <PrtctDt> [0..1] Date 754
     UncoveredProtectQuantity <UcvrdPrtctQty> [0..1] ± 755
   AdditionalInformation <AddtlInf> [0..1]  755
     AdditionalText <AddtlTxt> [0..*] Text 755
     PartyContactNarrative <PtyCtctNrrtv> [0..*] Text 755
   SupplementaryData <SplmtryData> [0..*] ± C29 755
13.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AdditionalInformationRule
All elements in the AdditionalInformation sequence must not contain information that can be
provided in a structured field unless bilaterally agreed.
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 736 February 2026
```

## File page 737

```text
C3 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C5 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C6 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 BeneficialOwnerBreakdownRequestRule
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
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C12 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 737 February 2026
```

## File page 738

```text
C13 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C14 EventTypeRule
EventType/Code OTHR must only be used in case no other corporate action event code is
appropriate.
EventType/Code CHAN must only be used in case no other corporate action event code is
appropriate and only for an event which relates to a change.
EventType/Code REDM must only be used when the redemption is decided by the issuer and
not by the securities holders.
C15 EventTypeRule
If Code is present, the code OTHR must only be used in case no other corporate action event
code is appropriate.
If Code is present, the code CHAN must only be used in case no other corporate action event
code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM must only be used when the redemption is decided by the
issuer and not by the securities holders.
C16 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C17 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C18 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C19 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C20 OptionNumberRule
For differentiation between options, the OptionNumber rather than the OptionType must be
used, for example, in the case where two or more offers can be described by the same
corporate action option code. Therefore, the OptionNumber value must be different for each
option.
C21 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 738 February 2026
```

