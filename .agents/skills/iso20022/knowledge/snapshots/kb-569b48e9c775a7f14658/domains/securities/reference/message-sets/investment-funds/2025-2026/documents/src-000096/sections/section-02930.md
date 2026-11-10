---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.2 CashOutPaymentInstrument <CshOutPmtInstrm>", "55.4.5.21.1.2.3 BankersDraftDetails <BkrsDrftDtls>", "55.4.5.21.1.2.3.3 DraweeIdentification <DrweeId>", "55.4.5.21.1.2.3.3.1 Party <Pty>", "55.4.5.21.1.2.3.3.1.2 BICFI <BICFI>"]
file_pages: [4101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.2.3.3.1.2 BICFI <BICFI>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4101 to 4101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4101

```text
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
55.4.5.21.1.2.3.3.1.2  BICFI <BICFI>
Presence: [1..1]
Definition: Identification of the financial institution expressed as a BIC.
Impacted by: C6 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 5390
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
55.4.5.21.1.2.3.3.1.3  ClearingSystemMemberIdentification <ClrSysMmbId>
Presence: [1..1]
Definition: Choice of identifier for a clearing system member, as assigned by the clearing system. In
some clearing systems, the accounts of the clearing system members are also assigned an identifier.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4101 May 2026
```

