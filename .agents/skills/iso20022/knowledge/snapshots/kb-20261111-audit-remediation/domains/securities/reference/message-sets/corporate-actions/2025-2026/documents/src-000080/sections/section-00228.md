---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.1 OptionNumber <OptnNb>"]
file_pages: [305]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.1 OptionNumber <OptnNb>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 305 to 305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 305

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     IssuePrice <IssePric> [0..1] ± 315
     GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 315
     GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 316
   ShareholderNumber <ShrhldrNb> [0..1] Text 316
   AdditionalInformation <AddtlInf> [0..1]  317
     InformationToComplyWith <InfToCmplyWth> [0..*] Text 317
     DeliveryDetails <DlvryDtls> [0..*] Text 317
     ForeignExchangeInstructionsAdditionalInformation
<FXInstrsAddtlInf>
[0..*] Text 317
     InstructionAdditionalInformation <InstrAddtlInf> [0..*] Text 317
Constraints
• OptionNumber1Rule
For differentiation between options, the OptionNumber rather than the OptionType must be used, for
example, in the case where two or more offers can be described by the same corporate action option
code. Therefore, the OptionNumber value must be different for each option.
• OptionNumber2Rule
When the CorporateActionInstruction is unsolicited, that is, the instruction has not been preceded by
a Corporate ActionNotification, then OptionNumber/code must be UNSO (unsolicited).
5.4.9.1  OptionNumber <OptnNb>
Presence: [1..1]
Definition: Number identifying the available corporate action options.
OptionNumber <OptnNb> contains one of the following elements (see "OptionNumber1Choice" on
page 970 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Text 970
Or}   Code <Cd> [1..1] CodeSet 970
5.4.9.2  OptionType <OptnTp>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 305 February 2026
```

