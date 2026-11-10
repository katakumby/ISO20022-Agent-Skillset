---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.49 GatingOrHoldBackDetails <GtgOrHldBckDtls>", "46.4.5.10.49.4 FinancialInstrumentIdentification <FinInstrmId>", "46.4.5.10.49.4.16 OtherProprietaryIdentification <OthrPrtryId>", "46.4.5.10.49.4.16.1 Identification <Id>"]
file_pages: [2476]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.49.4.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2476 to 2476.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2476

```text
46.4.5.10.49.4.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
46.4.5.10.49.4.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
46.4.5.10.49.5  FinancialInstrumentName <FinInstrmNm>
Presence: [0..1]
Definition: New name of the security.
Datatype: "Max350Text" on page 5403
46.4.5.10.49.6  RedemptionCompletion <RedCmpltn>
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
46.4.5.10.49.7  FinalConfirmation <FnlConf>
Presence: [0..1]
Definition: Indicates whether or not this is the final redemption confirmation in the execution of a gated
redemption.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2476 May 2026
```

