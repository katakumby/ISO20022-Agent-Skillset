---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["12 seev.040.001.13 CorporateActionInstructionCancellationRequestV13", "12.3 Constraints"]
file_pages: [722, 723]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.040.001.13"]
---

# 12.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 722 to 723.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 722

```text
12.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 BeneficialOwnerBreakdownRequestRule
If CorporateActionInstruction/OptionType/Code value is BOBD
(BeneficialOwnerBreakdownRequest), then CorporateActionGeneralInformation/EventType/
Code value must be WTRC (Withholding Tax Relief Certification).
(MT565 NVR C8)
On Condition
    /CorporateActionInstruction/OptionType/Code is equal to value 
'BeneficialOwnerBreakdownRequest'
Following Must be True
    /CorporateActionGeneralInformation/EventType/Code Must be equal to value 
'WithholdingTaxReliefCertification'
This constraint is defined at the MessageDefinition level.
C3 ChangeInstructionIndicatorGuideline
ChangeInstructionIndicator may only be used if CorporateActionOptionDetails/
WithdrawalAllowedIndicator was set to 'false' or '0' (No) in the CorporateActionNotification
message previously received and if CorporateActionOptionDetails/ChangeAllowedIndicator was
set to 'true' or '1' (Yes) in the CorporateActionNotification message previously received.
This constraint is defined at the MessageDefinition level.
C4 CorporateActionEventIdentificationRule
If the CorporateActionInstruction message was unsolicited (that is, this instruction has not been
preceded by a CorporateActionNotification), then, CorporateActionGeneralInformation/
CorporateActionEventIdentification must be NONREF.
This constraint is defined at the MessageDefinition level.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C7 DescriptionUsageRule
Description must be used alone as the last resort.
C8 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C9 EventTypeRule
EventType/Code OTHR must only be used in case no other corporate action event code is
appropriate.
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 722 February 2026
```

## File page 723

```text
EventType/Code CHAN must only be used in case no other corporate action event code is
appropriate and only for an event which relates to a change.
EventType/Code REDM must only be used when the redemption is decided by the issuer and
not by the securities holders.
C10 EventTypeRule
If Code is present, the code OTHR must only be used in case no other corporate action event
code is appropriate.
If Code is present, the code CHAN must only be used in case no other corporate action event
code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM must only be used when the redemption is decided by the
issuer and not by the securities holders.
C11 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C12 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C13 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
(COAF). Those recommendations are
available in the SMPG Global Market Practices Part 1 document on www.smpg.info.
C14 OptionNumber1Rule
For differentiation between options, the OptionNumber must be used (preferred rather than the
OptionType for example in the case where two or more offers can be described by the same
corporate action option code). Therefore, the OptionNumber value must be different for each
option.
C15 OptionNumber2Rule
When the CorporateActionInstruction is unsolicited, that is, the instruction has not been
preceded by an Corporate ActionNotification, then OptionNumber/code must be UNSO
(unsolicited).
C16 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C17 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C18 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
Approved by the Securities SEG on 27 January 2026 seev.040.001.13
CorporateActionInstructionCancellationRequestV13
Corporate Actions - Maintenance 2025 - 2026 723 February 2026
```

