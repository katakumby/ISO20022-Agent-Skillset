---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.19 RedemptionLegDetails <RedLegDtls>", "55.4.5.19.26 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "55.4.5.19.26.4 FinancialInstrumentIdentification <FinInstrmId>", "55.4.5.19.26.4.16 OtherProprietaryIdentification <OthrPrtryId>", "55.4.5.19.26.4.16.1 Identification <Id>"]
file_pages: [3928]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.19.26.4.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3928 to 3928.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3928

```text
55.4.5.19.26.4.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
55.4.5.19.26.4.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
55.4.5.19.26.5  FinancialInstrumentName <FinInstrmNm>
Presence: [0..1]
Definition: New name of the security.
Datatype: "Max350Text" on page 5403
55.4.5.19.26.6  RedemptionCompletion <RedCmpltn>
Presence: [0..1]
Definition: Specifies whether or not additional redemption order instructions are required in order for the
redemption to be completed.
Datatype: "RedemptionCompletion1Code" on page 5346
CodeName Name Definition
RED0 RedemptionNo It is not necessary to send more
redemption order instructions to the
executing party to complete the
redemption, the executing will generate
redemption confirmations automatically.
RED1 RedemptionYes Additional redemption order instructions
must be sent to the executing party order
to have the rest of the redemption
executed.
55.4.5.19.26.7  FinalConfirmation <FnlConf>
Presence: [0..1]
Definition: Indicates whether or not this is the final redemption confirmation in the execution of a gated
redemption.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 3928 May 2026
```

