---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.5 OptionFeatures <OptnFeatrs>", "7.4.13.5.1 Code <Cd>"]
file_pages: [432]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.5.1 Code <Cd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 432 to 432.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 432

```text
OptionFeatures <OptnFeatrs> contains one of the following OptionFeaturesFormat32Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 432
Or}   Proprietary <Prtry> [1..1] ± 433
7.4.13.5.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the features that may apply to a corporate action option.
Datatype: "OptionFeatures15Code" on page 1225
CodeName Name Definition
NOSE NoServiceOffered Feature whereby the holder must elect
directly to the issuer's agent (issuer only
supported option).
CAOS OptionApplicability Option applicability is not subject to the
account owner decision but depends on
the terms defined by the issuer, for
example in the case of equity linked
notes or warrants.
COND Conditional Feature whereby the holder can elect to
place a condition on the acceptance of
the option.
MAXC MaximumCash Maximum cash option, may be subject to
scaling, as such you may receive a
combination of cash and securities
outturn.
MAXS MaximumSecurities Maximum stock option, may be subject
to scaling, as such you may receive a
combination of securities and cash
outturn.
OPLF OddLotPreference Tender or exchange with the odd lot
preference.
PROR Proration Feature whereby the option can be
subject to pro ration in case, for
example, of over-subscription.
VVPR ReducedWithholdingTax Reduced withholding tax rate applies to
the option.
PINS PreviousInstructionInvalidity Indicates the previously sent instructions
becomes invalid. This is only applicable
after a market deadline extension.
ASVO AccountServicerOption Option is offered by the account servicer
only.
BOIS BeneficiaryOwnerInstruction Indicates that the holder needs to
instruct at beneficiary owner level only.
QCAS InstructCashAmount Feature whereby the holder should only
instruct a cash amount.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 432 February 2026
```

