---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["6 seev.034.001.16 CorporateActionInstructionStatusAdviceV16", "6.4 Message Building Blocks", "6.4.4 InstructionProcessingStatus <InstrPrcgSts>", "6.4.4.5 Pending <Pdg>", "6.4.4.5.2 PendingReason <PdgRsn>", "6.4.4.5.2.2 Reason <Rsn>", "6.4.4.5.2.2.1 ReasonCode <RsnCd>", "6.4.4.5.2.2.1.2 Proprietary <Prtry>"]
file_pages: [344]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.034.001.16"]
---

# 6.4.4.5.2.2.1.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 344 to 344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 344

```text
CodeName Name Definition
NTAX InconsistentTaxRate Tax rate is not consistent with the
documentation in place.
ITAX IncorrectTaxRate Tax rate provided is incorrect. It falls
outside the acceptable values for that
investment country.
IPED InstructionPriorToEntitlementDate Instruction was received prior to
entitlement date.
MONY InsufficientMoney Insufficient money in your account.
IPAW InvalidPaperwork Required paperwork is invalid,
incomplete or missing.
LACK LackOfSecurities Insufficient financial instruments in your
account.
LATE MarketDeadlineMissed Instruction was received after market
deadline.
MCER MissingCertification Awaiting receipt of adequate
certification.
MTAX MissingTaxRate Tax rate is missing.
OTHR Other Other. See Narrative.
FULL PendingBeneficiaryOwnerDetails Pending receipt of beneficiary owner
details.
PENR PendingReceipt Instruction is pending receipt of
securities, for example, from a purchase
or loan.
DQUA QuantityDisagreement Quantity of financial instruments does
not match.
SNAV SystemNotAvailable System is not available. Instruction is
sent outside of business hours.
CERT WrongCertificatesNumbers Certificate number error.
6.4.4.5.2.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Pending reason specified as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
6.4.4.5.2.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the processed instruction.
Approved by the Securities SEG on 27 January 2026 seev.034.001.16
CorporateActionInstructionStatusAdviceV16
Corporate Actions - Maintenance 2025 - 2026 344 February 2026
```

