---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.6 FiscalExemption <FsclXmptn>"]
file_pages: [4586]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.6 FiscalExemption <FsclXmptn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4586 to 4586.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4586

```text
66.1.24.4.6  FiscalExemption <FsclXmptn>
Presence: [0..1]
Definition: Indicates whether an owner of the account may benefit from a fiscal exemption or amnesty,
for example, when declaring overseas investments.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.24.4.7  SignatoryRightIndicator <SgntryRghtInd>
Presence: [0..1]
Definition: Indicates whether the signature of the account owner is required to authorise transactions on
the account.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.24.4.8  MiFIDClassification <MiFIDClssfctn>
Presence: [0..1]
Definition: Details about the MiFID classification of the account owner.
MiFIDClassification <MiFIDClssfctn> contains the following elements (see "MiFIDClassification1" on
page 4815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Classification <Clssfctn> [1..1] CodeSet 4815
   Narrative <Nrrtv> [0..1] Text 4816
66.1.24.4.9  Notification <Ntfctn>
Presence: [0..*]
Definition: Type of information that must be provided to the account holder.
Notification <Ntfctn> contains the following elements (see "Notification2" on page 4825 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NotificationType <NtfctnTp> [1..1] Text 4826
   Required <Reqrd> [1..1] Indicator 4826
   DistributionType <DstrbtnTp> [0..1] ± 4826
66.1.24.4.10  FATCAFormType <FATCAFormTp>
Presence: [0..*]
Definition: Type of Foreign Account Tax Compliance Act (FATCA) form submitted by the investor or
account owner.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4586 May 2026
```

