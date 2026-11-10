---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["13 seev.041.001.15 CorporateActionInstructionCancellationRequestStatusAdviceV15", "13.4 Message Building Blocks", "13.4.5 CorporateActionInstruction <CorpActnInstr>", "13.4.5.1 OptionNumber <OptnNb>"]
file_pages: [748]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.041.001.15"]
---

# 13.4.5.1 OptionNumber <OptnNb>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 748 to 748.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 748

```text
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• SafekeepingPlaceRule
SafekeepingPlace must only be used by global custodians that allow their clients to specify where
the securities are to be held, for example, in an ICSD account versus an account at the local CSD.
• StatusQuantityOrStatusCashAmount1Rule
If StatusQuantity is present, then StatusCashAmount is not allowed. (MT 567 C5).
On Condition
    /StatusQuantity is present
Following Must be True
    /StatusCashAmount Must be absent
• StatusQuantityOrStatusCashAmount2Rule
If StatusCashAmount is present, then StatusQuantity is not allowed. (MT 567 C5).
On Condition
    /StatusCashAmount is present
Following Must be True
    /StatusQuantity Must be absent
13.4.5.1  OptionNumber <OptnNb>
Presence: [1..1]
Definition: Number identifying the available corporate action options.
OptionNumber <OptnNb> contains one of the following elements (see "OptionNumber1Choice" on
page 970 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Number <Nb> [1..1] Text 970
Or}   Code <Cd> [1..1] CodeSet 970
13.4.5.2  OptionType <OptnTp>
Presence: [1..1]
Definition: Specifies the corporate action options available to the account owner.
OptionType <OptnTp> contains one of the following elements (see "CorporateActionOption41Choice"
on page 913 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 914
Or}   Proprietary <Prtry> [1..1] ± 915
13.4.5.3  OptionFeatures <OptnFeatrs>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.041.001.15
CorporateActionInstructionCancellationRequestStat
usAdviceV15
Corporate Actions - Maintenance 2025 - 2026 748 February 2026
```

