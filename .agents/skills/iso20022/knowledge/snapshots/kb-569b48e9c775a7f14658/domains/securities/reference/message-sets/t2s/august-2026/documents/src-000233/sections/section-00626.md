---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.49 PrincipalPayingAgent <PrncplPngAgt>", "27.4.2.3.49.10 PrimaryCommunicationAddress <PmryComAdr>"]
file_pages: [811]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.49.10 PrimaryCommunicationAddress <PmryComAdr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 811 to 811.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 811

```text
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress3" on page 3099 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [1..1] CodeSet 3099
   MailingIndicator <MlngInd> [1..1] Indicator 3099
   RegistrationAddressIndicator <RegnAdrInd> [1..1] Indicator 3100
   NameAndAddress <NmAndAdr> [1..1] ± 3100
Constraints
• MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
27.4.2.3.49.10  PrimaryCommunicationAddress <PmryComAdr>
Presence: [0..1]
Definition: Communication device number or electronic address used for communication.
PrimaryCommunicationAddress <PmryComAdr> contains the following elements (see
"CommunicationAddress3" on page 3100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 3100
   Phone <Phne> [0..1] Text 3100
   Mobile <Mob> [0..1] Text 3101
   FaxNumber <FaxNb> [0..1] Text 3101
   TelexAddress <TlxAdr> [0..1] Text 3101
   URLAddress <URLAdr> [0..1] Text 3101
27.4.2.3.49.11  SecondaryCommunicationAddress <ScndryComAdr>
Presence: [0..1]
Definition: Communication device number or electronic address used for communication.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 811 August 2026
```

